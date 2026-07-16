def isAnagram(self, s: str, t: str) -> bool:
    """
    If len is diff, can't be anagram. Compare sorted strings
    Time: O(n logn)
    Space: O(1)

    if len(s) != len(t):
        return False
    
    return sorted(s) == sorted(t)
    """

    """
    Count number of chars in hash map and if the 2 hash maps are equal then the
    two strings are anagrams
    Time: O(n)
    Space: O(n)

    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
    """

