"""
Python3 program to scrape Project Euler data.
Could be used to automate script creation, analyse problem sets,
and as a helper tool for problem solving.
"""
import io
import os.path
import requests
from bs4 import BeautifulSoup


# A class to represent a Project Euler problem.
class Problem:
    # class variables
    attribution = "The following problem is taken from Project Euler."
    problem_number = 0
    problem_url = 'https://projecteuler.net/problem='
    minimal_url = 'https://projecteuler.net/minimal='
    soup = BeautifulSoup()
    title = ''
    content = ''
    timestamp = ''
    file_name = ''

    # constructor method
    def __init__(self, problem_number):
        self.problem_number = problem_number
        self.problem_url += str(problem_number)
        self.minimal_url += str(problem_number)
        self.soup = make_soup(self.problem_url)
        self.title = get_title(self.soup)
        self.content = get_content(make_soup(self.minimal_url))
        self.timestamp = get_timestamp(self.soup)
        self.file_name = f'problem_{problem_number}.py'

    # string representation
    def __str__(self):
        return f'Problem {self.problem_number}: {self.title}'

    # object representation
    def __repr__(self):
        return self.__str__()


# Returns a link to the current problem number
def make_soup(url):
    html = requests.get(url)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup


# Returns the problem title
def get_title(soup):
    title = str(soup.find('h2').text).upper()
    return title


# Parses and returns a cleaned up version of the content
def get_content(soup) -> list[str]:
    dirty_body = soup.findAll('p')
    cleaned_body = clean_body(dirty_body)
    return cleaned_body


# A helper function to clean up html tags from the parsed content
def clean_body(dirty_body):
    cleaned_body = []
    for line in dirty_body:
        cleaned_body.append(line.get_text())
    return cleaned_body


# Returns the date published, difficulty rating, and the number of people that solved the problem.
def get_timestamp(soup) -> list[str]:
    timestamp = str(soup.find('span', {"class": "tooltiptext_right"}).text)
    timestamp = timestamp.split(';')
    return timestamp


def boilerplate_code(number):
    two_lines = '\n\n'
    line_w_tab = '\n\t'
    code = f'{two_lines}def problem_{number}():{line_w_tab}answer = None{line_w_tab}return answer\n' + two_lines
    main = f'if __name__ == "__main__":{line_w_tab}print(problem_{number}())'
    return code + main


def lines_to_write(problem: Problem) -> list[str]:
    triple_quotes = '"""'
    lines = [triple_quotes, problem.attribution, problem.title, problem.problem_url, '\n'.join(problem.content),
             '\n'.join(problem.timestamp), triple_quotes]
    return lines


def write_to_py_file(problem: Problem, folder: str) -> bool:
    if os.path.isdir(folder):
        file_name = folder + problem.file_name
    else:
        file_name = problem.file_name

    if os.path.isfile(file_name):
        return False
    else:
        file = io.open(file_name, 'w', encoding='utf-8')
        file.write('\n\n'.join(lines_to_write(problem)))
        return True


def update_directory(start=1, end=1, folder='') -> str:
    number_of_updated_files = 0
    for problem_number in range(start, (end + 1)):
        problem = Problem(problem_number)
        if write_to_py_file(problem, folder):
            number_of_updated_files += 1
    return f'{number_of_updated_files} out of {end + 1 - start} added/updated.'


def ask_user_for_input():
    s = 1  # int(input("Enter the number for the first problem:\n"))
    e = 1  # int(input("Enter the number for the last problem:\n"))
    f = ''  # str(input("Enter path for storing files:\n"))
    return update_directory(s, e, f)


if __name__ == "__main__":
    print(ask_user_for_input())
