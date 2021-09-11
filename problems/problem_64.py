"""
Link: [https://projecteuler.net/problem=64]

The following problem is taken from Project Euler.

ODD PERIOD SQUARE ROOTS

All square roots are periodic when written as continued fractions and can be written in the form:
For example, let us consider $\sqrt{23}:$
If we continue we would get the following expansion:
The process can be summarised as follows:

$\quad \quad a_0=4, \frac 1 {\sqrt{23}-4}=\frac {\sqrt{23}+4} 7=1+\frac {\sqrt{23}-3} 7$
$\quad \quad a_1=1, \frac 7 {\sqrt{23}-3}=\frac {7(\sqrt{23}+3)} {14}=3+\frac {\sqrt{23}-3} 2$
$\quad \quad a_2=3, \frac 2 {\sqrt{23}-3}=\frac {2(\sqrt{23}+3)} {14}=1+\frac {\sqrt{23}-4} 7$
$\quad \quad a_3=1, \frac 7 {\sqrt{23}-4}=\frac {7(\sqrt{23}+4)} 7=8+\sqrt{23}-4$
$\quad \quad a_4=8, \frac 1 {\sqrt{23}-4}=\frac {\sqrt{23}+4} 7=1+\frac {\sqrt{23}-3} 7$
$\quad \quad a_5=1, \frac 7 {\sqrt{23}-3}=\frac {7 (\sqrt{23}+3)} {14}=3+\frac {\sqrt{23}-3} 2$

$\quad \quad a_6=3, \frac 2 {\sqrt{23}-3}=\frac {2(\sqrt{23}+3)} {14}=1+\frac {\sqrt{23}-4} 7$
$\quad \quad a_7=1, \frac 7 {\sqrt{23}-4}=\frac {7(\sqrt{23}+4)} {7}=8+\sqrt{23}-4$

It can be seen that the sequence is repeating. For conciseness, we use the notation $\sqrt{23}=[4;(1,3,1,8)]$, to indicate that the block (1,3,1,8) repeats indefinitely.
The first ten continued fraction representations of (irrational) square roots are:

$\quad \quad \sqrt{2}=[1;(2)]$, period=$1$
$\quad \quad \sqrt{3}=[1;(1,2)]$, period=$2$
$\quad \quad \sqrt{5}=[2;(4)]$, period=$1$
$\quad \quad \sqrt{6}=[2;(2,4)]$, period=$2$
$\quad \quad \sqrt{7}=[2;(1,1,1,4)]$, period=$4$
$\quad \quad \sqrt{8}=[2;(1,4)]$, period=$2$
$\quad \quad \sqrt{10}=[3;(6)]$, period=$1$
$\quad \quad \sqrt{11}=[3;(3,6)]$, period=$2$
$\quad \quad \sqrt{12}=[3;(2,6)]$, period=$2$
$\quad \quad \sqrt{13}=[3;(1,1,1,1,6)]$, period=$5$

Exactly four continued fractions, for $N \le 13$, have an odd period.
How many continued fractions for $N \le 10\,000$ have an odd period?

Published on Friday, 27th February 2004, 06:00 pm; Solved by 21948;Difficulty rating: 20%
"""


def problem_64():
	answer = None
	return answer


if __name__ == "__main__":
	print(problem_64())