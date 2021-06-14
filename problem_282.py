"""
The following problem is taken from Project Euler.

THE ACKERMANN FUNCTION


For non-negative integers $m$, $n$, the Ackermann function $A(m,n)$ is defined as follows:

$$
A(m,n) = \cases{
n+1 &$\htmltext{ if  }m=0$\cr
A(m-1,1) &$\htmltext{ if   }m>0 \htmltext{  and  } n=0$\cr
A(m-1,A(m,n-1)) &$\htmltext{ if   }m>0 \htmltext{  and  } n>0$\cr
}$$


For example $A(1,0) = 2$, $A(2,2) = 7$ and $A(3,4) = 125$.


Find $\displaystyle\sum_{n=0}^6 A(n,n)$ and give your answer mod $14^8$.

Published on Friday, 12th March 2010, 05:00 pm; Solved by 939;Difficulty rating: 70%
"""
