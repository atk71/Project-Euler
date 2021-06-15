"""
Link: [https://projecteuler.net/problem=568]

The following problem is taken from Project Euler.

RECIPROCAL GAMES II

Tom has built a random generator that is connected to a row of $n$ light bulbs. Whenever the random generator is activated each of the $n$ lights is turned on with the probability of $\frac 1 2$, independently of its former state or the state of the other light bulbs.
While discussing with his friend Jerry how to use his generator, they invent two different games, they call the reciprocal games:
Both games consist of $n$ turns. Each turn is started by choosing a number $k$ randomly between (and including) $1$ and $n$, with equal probability of $\frac 1 n$ for each number, while the possible win for that turn is the reciprocal of $k$, that is $\frac 1 k$.
In game A, Tom activates his random generator once in each turn. If the number of lights turned on is the same as the previously chosen number $k$, Jerry wins and gets $\frac 1 k$, otherwise he will receive nothing for that turn. Jerry's expected win after playing the total game A consisting of $n$ turns is called $J_A(n)$. For example $J_A(6)=0.39505208$, rounded to 8 decimal places.
For each turn in game B, after $k$ has been randomly selected, Tom keeps reactivating his random generator until exactly $k$ lights are turned on. After that Jerry takes over and reactivates the random generator until he, too, has generated a pattern with exactly $k$ lights turned on. If this pattern is identical to Tom's last pattern, Jerry wins and gets $\frac 1 k$, otherwise he will receive nothing. Jerry's expected win after the total game B consisting of $n$ turns is called $J_B(n)$. For example $J_B(6)=0.43333333$, rounded to 8 decimal places.
Let $D(n)=J_B(n)−J_A(n)$. For example, $D(6) = 0.03828125$.
Find the 7 most significant digits of $D(123456789)$ after removing all leading zeros.
(If, for example, we had asked for the 7 most significant digits of $D(6)$, the answer would have been 3828125.)

Published on Saturday, 3rd September 2016, 04:00 pm; Solved by 249;Difficulty rating: 55%
"""


def problem_568():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_568())