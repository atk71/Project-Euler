import io
import os.path
import requests
from bs4 import BeautifulSoup


def make_soup(url):
    html = requests.get(url)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'html.parser')
        return soup


def scrape_title(soup):
    attribution = "The following problem is taken from Project Euler.\n\n"
    title = str(soup.find('h2').text).upper()
    return f'{attribution}{title}\n\n'


def scrape_body(soup):
    dirty_body = soup.findAll('p')
    cleaned_body = clean_body(dirty_body)
    return cleaned_body


def scrape_timestamp(soup):
    timestamp = str(soup.find('span', {"class": "tooltiptext_right"}).text)
    return f'\n{timestamp}\n'


def clean_body(dirty_body):
    cleaned_body = []
    for line in dirty_body:
        cleaned_body.append(f'{line.get_text()}\n')
    return cleaned_body


def boilerplate_code(number):
    two_lines = '\n\n'
    line_w_tab = '\n\t'
    code = f'{two_lines}def problem_{number}():{line_w_tab}answer = None{line_w_tab}return answer\n' + two_lines
    main = f'if __name__ == "__main__":{line_w_tab}print(problem_{number}())'
    return code + main


def write_to_py_file(number, title, content, timestamp):
    file_name = f'problem_{number}.py'
    if os.path.isfile(file_name):
        file = io.open(file_name, 'w', encoding='utf-8')
        triple_quotes = '"""\n'
        file.write(triple_quotes)
        file.write(title)
        for result in content:
            file.write(result)
        file.write(timestamp)
        file.write(triple_quotes)
        file.write(boilerplate_code(number))


def update_directory(start, end):
    for question_number in range(start, (end + 1)):
        euler_url = make_soup(f'https://projecteuler.net/problem={question_number}')
        euler_minimal_url = make_soup(f'https://projecteuler.net/minimal={question_number}')
        page_title = scrape_title(euler_url)
        page_content = scrape_body(euler_minimal_url)
        page_timestamp = scrape_timestamp(euler_url)
        write_to_py_file(question_number, page_title, page_content, page_timestamp)
    print("update complete!")


def ask_user_for_input():
    s = int(input("Enter the number for the first problem:\n"))
    e = int(input("Enter the number for the last problem:\n"))
    update_directory(s, e)


def prepend_link(start, end):
    for question_number in range(start, (end + 1)):
        file_name = f'problem_{question_number}.py'
        if os.path.isfile(file_name):
            file = io.open(file_name, 'r')
            save = file.read()
            file = io.open(file_name, 'w', encoding='utf-8')
            file.write(f'# https://projecteuler.net/problem={question_number}')
            file = io.open(file_name, 'a', encoding='utf=8')
            file.write(save)


if __name__ == "__main__":
    prepend_link(1, 759)
