"""
Link: [https://projecteuler.net/problem=17]

The following problem is taken from Project Euler.

NUMBER LETTER COUNTS

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Published on Friday, 17th May 2002, 06:00 pm; Solved by 152573;Difficulty rating: 5%
"""


def number_to_words(number: int) -> str:
	ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
	teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
	tens = {0: ones, 1: teens, 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
	hundred = 'hundred'
	thousand = 'thousand'
	and_symbol = 'and'
	words = teens[(number % 5)]
	print(words)

	return words


def count_letters_in_words(number: int) -> int:
	words = number_to_words(number)
	return len(words.replace('-', '').replace(' ', ''))


def number_letter_counts() -> int:
	start = 1
	end = 1000
	letter_count = 0
	for i in range(start, end + 1):
		letter_count += count_letters_in_words(i)
	return letter_count


if __name__ == "__main__":
	print(number_letter_counts())
