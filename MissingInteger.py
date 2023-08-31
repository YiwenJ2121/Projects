'''
Write a function:
    class Solution { public int solution(int[] A); }
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
''' The following is an OK solution:
def solution(A):
    n = len(A)
    if n==0:
        return 1
    A.sort()
    if A[0] > 0 and A[0] != 1:
        return 1
    for i in range(n-1):
        if (A[i]<=0 and A[i+1]>1):
            return 1
        if (A[i]>0 and A[i+1]-A[i]>1):
            return A[i]+1
    return max(A[n-1]+1, 1) # in case the whole array is non-positive
'''
'''A better solution:
n = len(A). There can at most n positive integers in A, namely 1 ... n. The missing positive integer must be in the range
 1 ... n. So, create a count array of length n for A, then find the first missing positive integer. 
 We don't need to worry about negative numbers or numbers greater than n in A.
'''
def solution(A):
    n = len(A)
    if n == 0:
        return 1
    counts = [False]*n
    for i in range(n):
        if A[i] > 0 and A[i] <= n and counts[A[i]-1] == False:  # don't need to consider A[i]>n
            counts[A[i]-1] = True
    for j in range(n):
        if counts[j] == False:
            return j+1
    return n+1

A = [-1, -2, 0]
B = []
C = [-8, 3, 5]
D = [-6, 1, 9, 6, 3, 4]
E = [3]
F = [6, 2, 4]
print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))
print(solution(E))
print(solution(F))