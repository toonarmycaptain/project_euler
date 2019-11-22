import os

from pathlib import Path

import requests

from bs4 import BeautifulSoup
from html2text import html2text


def make_files():
    # Ensure cwd is dir of script.
    parent_dir = Path(__file__).parent
    os.chdir(parent_dir)

    # Get next problem
    latest_problem_num: int = int(max(str(folder)[-1] for folder in parent_dir.iterdir()
                                      if folder.is_dir() and str(folder)[-1].isdigit()
                                      ))

    new_problem_num = latest_problem_num + 1

    make_folder_and_files(new_problem_num)


def make_folder_and_files(problem_number: int):
    # Create folder
    problem_folder_path = Path(f'problem_{problem_number}')
    problem_folder_path.mkdir(exist_ok=True)

    with open(Path(problem_folder_path, '__init__.py'), 'w+') as init:
        init.write('')

    with open(Path(problem_folder_path, f'problem_{problem_number}_solution.py'), 'w+') as solution:
        solution.write(f'"""'
                       f'Project Euler problem {problem_number} solution\n\n'
                       f'{get_problem_text(problem_number)}'
                       f'"""')

    with open(Path(problem_folder_path, f'test_problem_{problem_number}_solution.py'), 'w+') as test_file:
        test_file.write(f'"""Tests for Project Euler problem {problem_number}"""')


def get_problem_text(problem_number: int):
    problem_page_html = requests.get(f'https://projecteuler.net/problem={problem_number}').content

    problem_page_soup = BeautifulSoup(problem_page_html, 'html.parser')
    problem_html = problem_page_soup.find('div', attrs={"class": "problem_content"})
    problem_text = html2text(str(problem_html))
    return problem_text


if __name__ == '__main__':
    make_files()
