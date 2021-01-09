from db_utils import run_query
from collections import Counter
from file_ops import write_csv_from_dict
from constants import modules_file


def insert_into_repos_table(repo_url, requirements_url):
    sql_query = """insert into repos(repo_url, requirements_url) values (%s, %s)"""
    run_query(sql_query, [repo_url, requirements_url])


def get_repo_id(path):
    sql_query = ("""select repo_id from repos where requirements_url='%s' """ % (path))
    repo_id = run_query(sql_query)[0]['repo_id']
    return repo_id


def insert_into_requirement_table(repo_id, module_name):
    sql_query = """insert into requirements(repo_id, requirement) values (%s, %s)"""
    run_query(sql_query, [repo_id, module_name])


def get_module_names():
    sql_query = """select requirement from requirements"""
    modules = run_query(sql_query)
    module_names = [module['requirement'].lower() for module in modules]
    return module_names


def get_top_modules():
    modules = get_module_names()
    fieldnames = ['module_name', 'module_count']
    module_count = [{'module_name': module, 'module_count': count} for (module, count) in Counter(modules).most_common()]
    write_csv_from_dict(modules_file, fieldnames, module_count)


if __name__ == "__main__":
    get_top_modules()