'''
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R]
(0 ≤ P < Q < R < N).
For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:
        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:
    class Solution { public int solution(int[] A); }
that, given a non-empty array A, returns the value of the maximal product of any triplet.
For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
'''
''' Thoughts:
sort A. check the sign of two ends. 
'''

def solution(A):
    A.sort()
    print(A)
    if A[-1] <= 0:
        return A[-1] * A[-2] * A[-3]
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

A = [-3, -4, -5, -1, 0]
B = [-5, -1, -6, -2, -2]
C = [6, -2, -1, -7, -2, -3]
D = [5, -3, -4, -2, -1, 0]
E = [3, 9, 0, -3, -4, -1, -2]
F = [2, 1, 1, 3, -6, -4, -5]
print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))
print(solution(E))
print(solution(F))
