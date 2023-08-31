'''
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river
(position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.
You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where
one leaf falls at time K, measured in seconds.The goal is to find the earliest time when the frog can jump to the other
side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is,
we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the
speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in
the river.
For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:
    class Solution { public int solution(int X, int[] A); }
that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump
to the other side of the river.
If the frog is never able to jump to the other side of the river, the function should return −1.
For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:
        N and X are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..X].
'''
''' Thoughts:
1. Create an array of length X containing all false. Each element represent if the leaf at position (i+1) has fallen. 
The goal is to find the index in A where all elements in X are true. This can be checked using all(A). If all(A) is true,
then there is no false in A. O(n2)
2. Create an array of boolean values that represents if a leaf at a 
particular position has fallen. Create an integer representing the number of positions needed. If one element in the 
boolean array is true, reduce the integer by 1. When the integer is 0, all positions are covered. O(n)
'''

def solution(X, A):
    n = len(A)
    time = -1
    if n >= X:
        positions = [False] * X
        for i in range(n):
            if positions[A[i]-1] == False:
                positions[A[i] - 1] = True
                X -= 1
            if X == 0:
                time = i
                break
    return time

A = [1, 5, 3, 2, 6, 4, 2, 6, 7, 5, 3, 1, 2, 9, 3, 4, 8]
print(solution(9, A))
B = [1, 5, 3, 2, 6, 4, 2, 6, 7, 5, 3]
print(solution(7, B))
C = [1, 1, 1]
print(solution(1, C))
D = [1, 3, 1, 2, 3]
print(solution(3, D))
E = [5, 3, 1, 3, 4, 4, 1, 2, 3]
print(solution(5, E))
