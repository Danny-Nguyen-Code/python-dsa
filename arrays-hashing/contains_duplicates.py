def contains_duplicates(self, nums: List[int]) -> bool:
    """
    brute force:
    Time: O(n^2)
    Space: O(1)

    * times out from last case
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]: return True
    return False
    """

    """
    sort list in order, and duplicates will appear next to each other:
    Time: O(n logn)
    Space: O(1) (or O(n) depending on sortin algorithm)

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]: return True
    return False
    """

    """
    hash set:
    Time: O(n)
    Space: O(n)

    seen = set()
    for num in nums:
        if num in seen: return True
        seen.add(num)
    return False
    """

    """
    hash set length: if length of hash set is < list, there are dupes
    Time: O(n)
    Space: O(n)

    return len(set(nums)) < len(nums)
    """