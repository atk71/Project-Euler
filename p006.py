"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is, 385
The square of the sum of the first ten natural numbers is, 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def solve():
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, 101):
        sum_of_squares += (i * i)
        print(sum_of_squares)
        square_of_sum += i
        print(square_of_sum)
    return (square_of_sum * square_of_sum) - sum_of_squares


print(solve())
