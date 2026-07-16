def isAnagram(self, s: str, t: str) -> bool:
    """
    If len is diff, can't be anagram. Compare sorted strings
    if len(s) == len(t):
        return False
    
    return sorted(s) == sorted(t)
    """

    