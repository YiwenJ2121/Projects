'''
You are given N counters, initially set to 0, and you have two possible operations on them:
        increase(X) − counter X is increased by 1,
        max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:
        if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
        if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:
    class Solution { public int[] solution(int N, int[] A); }
that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing
the values of the counters.
Result array should be returned as an array of integers.
For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:
        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].
'''
''' The following code failed the time complexity requirement
def solution(N, A):
    counters = [0] * N
    maxCount = 0
    print(counters)
    for x in A:
        if x > N:
            counters = [maxCount] * N  #****** This step is O(n)
        else:
            counters[x-1] += 1
            maxCount = max(maxCount, counters[x-1])
        print(counters)
    return counters
'''
''' Thoughts
When A[i] < N, A[i] stays the same or is updated to the currentMax before it's incremented by 1. A[i] is updated if A[i-1]
was greater than N. All elements that are supposed to be incremented after being maxed would be updated to max first, and 
then be incremented. Those that are not incremented after maxing stayed below currentMax, and therefore, need to be 
updated to currentMax in the second loop. "currentMax" functions as a switch, indicating the update of the new max.It 
can be a boolean value too.
'''
def solution(N, A):
    counters = [0] * N
    maxCount = 0
    currentMax = 0
    #print(counters)
    for x in A:
        if x > N:
            currentMax = maxCount
            #print("currentMax = " + str(currentMax))
        else:
            counters[x-1] = max(currentMax, counters[x-1])
            counters[x-1] += 1
            maxCount = max(maxCount, counters[x-1])
        #print(counters)
    for i in range(N):
        if counters[i] < currentMax:
            #print("here")
            counters[i] = currentMax
       # print(counters)
    return counters

print(solution(3, [1, 3, 1, 4]))
print(solution(1, [2, 1, 1, 2, 1]))
print(solution(4, [1, 4, 3, 1, 2, 4, 3]))