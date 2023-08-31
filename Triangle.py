'''
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].
For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.
Write a function:
    class Solution { public int solution(int[] A); }
that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and
returns 0 otherwise.
For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5    A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''

def solution(A):
    n = len(A)
    if n < 3:
        return False
    A.sort()
    if A[-1] <= 0 or A[-2] <= 0 or A[-3] <= 0:
        return False
    print(A)
    i = n - 1
    while i > 1 and A[i-2] > 0:
        print("i = " + str(i))
        if A[i] - A[i-1] < A[i-2]:
            return True
        i -= 1
    return False

K = [10, 50, 5, 1]
print(solution(K))

A = []
B = [2, 3]
C = [2, -3, 0]
D = [0, -3, 4, 2]
E = [-2, 3, 4, 7, 11, 18]
F = [1, 1, 23, 4, 7, 11, 13, 3]

print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))
print(solution(E))
print(solution(F)) 