'''
Write a function
    class Solution { public int solution(int[] A); }
that, given an array A consisting of N integers, returns the number of distinct values in array A.
For example, given array A consisting of six elements such that:
 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
''' Thoughts:
store every element in A into a set. then find the size of the set. Time complexity is O(n)
'''
def solution(A):
    distinctNum = 0
    n = len(A)
    helperSet = set()
    if n > 0:
        for i in range(n):
            helperSet.add(A[i])
    distinctNum = len(helperSet)
    return distinctNum

A = []
B = [2, 1, 6, 1, 2, 3, -6]
C = [1, 1, 1, 1, 1]
D = [1, 2, -3, 4]
print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))