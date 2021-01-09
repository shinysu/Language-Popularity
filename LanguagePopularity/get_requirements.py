import requests
import os
import requirements
from file_ops import read_csv_from_dict
from utils import insert_into_repos_table, insert_into_requirement_table, get_repo_id
from credentials import GITHUB_TOKEN_ID
from constants import projects_info_file

token = os.getenv('GITHUB_TOKEN', GITHUB_TOKEN_ID)


def get_requirements_data():
    """
    Read the url of the projects from projects_info_file and get the requirements.txt file for the projects
    """
    urls = read_csv_from_dict(projects_info_file)
    headers = {'Authorization': f'token {token}'}
    for path in urls:
        try:
            url = path + '/contents/requirements.txt'
            results = requests.get(url, headers=headers, timeout=5).json()
            if 'download_url' in results:
                insert_into_repos_table(url, results['download_url'])
                parse_requirements_data(results['download_url'])
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


def parse_requirements_data(path):
    """
    Scan the requirements.txt file and parse it using requirements module to get the module names
    """
    req = requests.get(path).text
    repo_id = get_repo_id(path)
    try:
        for module in requirements.parse(req):
            if module.name:
                insert_into_requirement_table(repo_id, module.name)
    except:
        print("Parse Error")


if __name__ == '__main__':
    get_requirements_data()