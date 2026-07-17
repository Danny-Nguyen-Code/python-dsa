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
    Space: O(1) because we can only have at most 26 characters

    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
    """

    """
    Create hash map array of all letters, increment and decrement for 1st and
    2nd string. Go through the array at the end and if any value is != 0, return
    False
    Time: O(n)
    Space: O(1) because can only have 26 chars
    
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    for val in count:
        if val != 0:
            return False
    return True
    """

isAnagram("burrito", "rrutiob")