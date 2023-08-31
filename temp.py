def buddyStrings(s, goal):
    ls = len(s)
    lg = len(goal)
    if ls != lg or ls < 2:
        return False
    diffCount = 0
    swap1 = 0
    swap2 = 0
    for i in range(ls):
        if s[i] != goal[i]:
            diffCount += 1
            if diffCount == 1:
                swap1 = i
            if diffCount == 2:
                swap2 = i
            if diffCount > 2:
                return False
    if diffCount < 2:
        return False
    if s[swap1] == goal[swap2] and s[swap2] == goal[swap1]:
        return True
    return False


s = "abc"
g = "k"
print(buddyStrings(s, g))
s1 = "c"
g1 = "d"
print(buddyStrings(s1, g1))
s1 = "aeiou"
g1 = "oeiau"
print(buddyStrings(s1, g1))
s2 = "ab"
g2 = "ab"
print(buddyStrings(s2, g2))