"""
The following problem is taken from Project Euler.

LOW-PRIME CHESSBOARD NIM

The game may start with any arrangement of $c$ coins in squares on the board. It is possible at any time for more than one coin to occupy the same square on the board at the same time. The coins are distinguishable, so swapping two coins gives a different arrangement if (and only if) they are on different squares.
On a given turn, the player must choose a coin and move it either left or up $2$, $3$, $5$, or $7$ spaces in a single direction. The only restriction is that the coin cannot move off the edge of the board.
The game ends when a player is unable to make a valid move, thereby granting the other player the victory.
Assuming that Alice goes first and that both players are playing optimally, let $M(n, c)$ be the number of possible starting arrangements for which Alice can ensure her victory, given a board of size $n$ by $n$ with $c$ distinct coins.
For example, $M(3, 1) = 4$, $M(3, 2) = 40$, and $M(9, 3) = 450304$.
What are the last $9$ digits of $M(10\,000\,019, 100)$?

Published on Saturday, 29th December 2018, 01:00 pm; Solved by 347;Difficulty rating: 30%
"""


def problem_649():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_649())