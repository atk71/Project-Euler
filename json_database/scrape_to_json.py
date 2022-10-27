"""
Python3 program to scrape Project Euler data.
Could be used to automate script creation, analyse problem sets,
and as a helper tool for problem solving.
"""
import io
import json
import os.path
import subprocess
import requests
import spacy
from bs4 import BeautifulSoup
from extract_keywords import extract_keywords

nlp = spacy.load("en_core_web_lg")

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
    file_name = 'json_database.json'

    # constructor method
    def __init__(self, problem_number):
        self.problem_number = problem_number
        self.problem_url += str(problem_number)
        self.minimal_url += str(problem_number)
        self.soup = make_soup(self.problem_url)
        self.title = get_title(self.soup)
        self.content = get_content(make_soup(self.minimal_url))
        self.timestamp = get_timestamp(self.soup)

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


def keyword_gen(title: str, content: list[str]):
    triple_quotes = '"""'
    sequence = triple_quotes + title + " " + '\n'.join(content) + triple_quotes
    # load the (small/large) engine language model
    # model_size = 'lg'  # (sm/lg)
    # language_model = "en_core_web_" + model_size
    # subprocess_call = "python -m spacy download " + language_model
    # subprocess.call(subprocess_call, shell=True)
    return extract_keywords(nlp, sequence)


def get_dictionary(problem: Problem):
    data = {'number': problem.problem_number,
            'title': problem.title,
            'content': keyword_gen(problem.title, problem.content),
            'date published': problem.timestamp[0],
            'solved by': problem.timestamp[1],
            'difficulty': problem.timestamp[2]
            }
    return data


def lines_to_write(problem: Problem) -> list[str]:
    triple_quotes = '"""'
    lines = [triple_quotes, problem.attribution, problem.title, problem.problem_url, '\n'.join(problem.content),
             '\n'.join(problem.timestamp), triple_quotes]
    return lines


def write_to_json_file(problem: Problem, folder: str) -> bool:
    if os.path.isdir(folder):
        file_name = folder + problem.file_name
    else:
        file_name = problem.file_name

    file = io.open(file_name, 'a', encoding='utf-8')
    file.write(json.dumps(get_dictionary(problem)) + '\n')
    return True


def update_dictionary(start=1, end=1, folder='') -> str:
    number_of_updated_files = 0
    for problem_number in range(start, (end + 1)):
        problem = Problem(problem_number)
        write_to_json_file(problem, folder)
        number_of_updated_files += 1
    return f'{number_of_updated_files} out of {end + 1 - start} added/updated.'


def ask_user_for_input():
    s = 1  # int(input("Enter the number for the first problem:\n"))
    e = 763  # int(input("Enter the number for the last problem:\n"))
    f = ''  # str(input("Enter path for storing files:\n"))
    return update_dictionary(s, e, f)


if __name__ == "__main__":
    print(ask_user_for_input())
