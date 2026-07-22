def groupAanagrams(self, strs:List[str]) ->List[List[str]]:
    """
    Sorting
    Time: O(n^2 logn)
    Space: O(n^2)

    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())
    """

    """
    Hash table
    Time: O(n^2)
    Space: O(n^2)

    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())
    """

def main():
    # groupAnagrams()

if __name__ == "__main__":
    main() 