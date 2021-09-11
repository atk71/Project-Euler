"""
Link: [https://projecteuler.net/problem=6]

The following problem is taken from Project Euler.

SUM SQUARE DIFFERENCE

The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Published on Friday, 14th December 2001, 06:00 pm; Solved by 495722;Difficulty rating: 5%
"""


def sum_square_difference() -> int:
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, 101):
        sum_of_squares += (i * i)
        square_of_sum += i
    return (square_of_sum * square_of_sum) - sum_of_squares


if __name__ == "__main__":
    print(sum_square_difference())  # 25164150
