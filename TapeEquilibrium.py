''' Question:
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P],
A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:
        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:
    class Solution { public int solution(int[] A); }
that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
'''
''' Thoughts:
Create an array of prefix sums and an array of suffix sums, then find the minimal difference between prefixSum[p] and suffixSum[n-p]
'''

def solution(A):
    print("A = ", end = "")
    print(A)
    n = len(A)
    prefixSum = [0]*(n+1)
    suffixSum = [0]*(n+1)
    for i in range(n):
        prefixSum[i+1] = A[i] + prefixSum[i]
        suffixSum[i+1] = A[n-1-i] + suffixSum[i]
    print("prefixSum = ", end = "")
    print(prefixSum)
    print("sufixSum = ", end="")
    print(suffixSum)
    diff = abs(prefixSum[1] - suffixSum[n-1])
    for i in range(1, n):
        diff = min(diff, abs(prefixSum[i]-suffixSum[n-i]))
    return diff

A = [1, 2, 3, 4, 5]
print(solution(A))
B = [3, 1, 2, 4, 3]
print(solution(B))
C = [-64, 2]
print(solution(C))
D = [-1, -2, -3, 4, 5, 60]
print(solution(D))
E = [60, 5, 4, -1, -2, -3]
print(solution(E))