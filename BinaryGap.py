''' Question:
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both
ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary
representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no
binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:
    class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N
doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].
'''
''' Thoughts:
2**31=2,147,483,648. So, N is maximally 32-1=31-digit long. Create a list of binary representation of N, then calculate 
prefix sum. Record the index of the first occurrence of 1, and the index when the sum changes. The max difference between 
the two indices is the binary gap.
'''

def solution(N):
    binaryRep = []
    while(N//2 > 0):
        remainder = N%2
        binaryRep = [remainder]+binaryRep
        N //= 2;
        if N//2 == 0:
            binaryRep = [N%2]+binaryRep
    print(binaryRep)
    startIndex = 0
    endIndex = 0
    binaryGap = 0;
    for x in range(1, len(binaryRep)):
        if binaryRep[x] == 1:
            startIndex = endIndex
            endIndex = x
            binaryGap = max(endIndex-startIndex-1, binaryGap)
    return binaryGap

print(solution(65))
