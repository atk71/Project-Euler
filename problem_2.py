"""
Link: [https://projecteuler.net/problem=2]

The following problem is taken from Project Euler.

EVEN FIBONACCI NUMBERS

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Published on Friday, 19th October 2001, 06:00 pm; Solved by 770300;Difficulty rating: 5%
"""
FIBONACCI_SERIES = {}


def fibonacci(nth_term):
    if nth_term in FIBONACCI_SERIES:
        return FIBONACCI_SERIES[nth_term]
    if nth_term <= 2:
        return 1
    FIBONACCI_SERIES[nth_term] = fibonacci(nth_term - 1) + fibonacci(nth_term - 2)
    return FIBONACCI_SERIES[nth_term]


def sum_even_fibonacci_numbers():
    answer = 0
    term_ceiling = 4000000
    term_count = 1
    term = 1
    while term < term_ceiling:
        term = fibonacci(term_count)
        if term % 2 == 0:
            answer += term
        term_count += 1
    return answer


if __name__ == "__main__":
    print(sum_even_fibonacci_numbers())  # 4613732
