''' Question
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element
of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

        the elements at indexes 0 and 2 have value 9,
        the elements at indexes 1 and 3 have value 3,
        the elements at indexes 4 and 6 have value 9,
        the element at index 5 has value 7 and is unpaired.

Write a function:

    class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

        N is an odd integer within the range [1..1,000,000];
        each element of array A is an integer within the range [1..1,000,000,000];
        all but one of the values in A occur an even number of times.
'''
''' Thoughts
1. Create an array representing the occurrence of each element, then iterate through the new array and search for the 
only odd number in it. The index of the odd number is the result.
This method could take too much space if the biggest number in A is 1 billion. 

2. Sort A, then check if every even-indexed element if the same as the one next to it. If not, then that even-indexed 
element is what we are looking for. 
Think: if the odd element happened at index 0, index n-1. if A has only 1 element.
'''

def solution(A):
    n = len(A)
    if n==1:
        return A[0]
    A.sort()
    print(A)
    unpaired = A[0]
    for i in range(0, n, 2):
        if (i == n-1 and A[i] != A[i-1]):
            unpaired = A[i]
            break
        if (A[i] != A[i+1]):
            unpaired = A[i]
            break
    return unpaired

A = [1, 2, 3, 6, 3, 2, 6]
print(solution(A))
B = [2, 1, 3, 2, 1, 4, 3]
print(solution(B))
C = [1, 6, 1, 3, 4, 6, 3, 4, 3]
print(solution(C))
D = [2]
print(solution(D))