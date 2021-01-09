"""
app.py - get the top modules used by Python projects from GitHub
"""
import requests
import os
from file_ops import write_csv_from_dict
from credentials import GITHUB_TOKEN_ID
from constants import projects_info_file, github_api_request_url
from get_requirements import get_requirements_data
from utils import get_top_modules

token = os.getenv('GITHUB_TOKEN', GITHUB_TOKEN_ID)


def get_repo_url():
    """
    Get the name, description, forks, stars, last update date and number of contributors for Python projects using
    GitHub api and writes the details to the project_info_file
    """
    url = github_api_request_url
    results = get_data(url)
    repos = get_required_data(results.json())
    fieldnames = ['name', 'description', 'url', 'forks', 'stars', 'last_push', 'contributors']
    '''while 'next' in results.links.keys():
        results = get_data(results.links['next']['url'])
        repos.extend(get_required_data(results.json()))'''
    write_csv_from_dict(projects_info_file, fieldnames, repos)


def get_data(url):
    """
    gets data from the url using requests module
    """
    headers = {'Authorization': f'token {token}'}
    try:
        results = requests.get(url, headers=headers, timeout=5)
        return results
    except requests.ConnectionError as e:
        print("Connection Error. Make sure you are connected to Internet.\n")
        print(str(e))
    except requests.Timeout as e:
        print("Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print("General Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Keyboard interrupt")


def get_required_data(results):
    """
    organises data to be pushed into projects_info_file
    """
    repo_details = []
    for repo in results['items']:
        contributors = len(get_data(repo['contributors_url']).json())
        data = {
            'name': repo['name'],
            'description': repo['description'],
            'url': repo['url'],
            'forks': repo['forks_count'],
            'stars': repo['stargazers_count'],
            'last_push': repo['pushed_at'],
            'contributors': contributors
        }
        repo_details.append(data)
    return repo_details


if __name__ == "__main__":
    get_repo_url()
    get_requirements_data()
    get_top_modules()
