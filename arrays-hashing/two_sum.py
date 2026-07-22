def main():
    twoSum([1, 3, 4, 6, 13], 17)

def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    brute force solution
    Time: O(n^2)
    Space: O(1)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] +nums[j] == target:
                return [i, j]
    return []
    """

    """
    sort array and use 2 pointers
    Time: O(n logn)
    Space: O(n)

    A = []
    for i, num in enumerate(nums):
        A.append([num, i])

    A.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        curr = A[i][0] + A[j][0]
        if curr == target:
            return [min(A[i][1], A[j][1]), 
                    max(A[i][1], A[j][1])]
        elif curr < target:
            i += 1
        else:
            j -= 1
    return []
    """

    """
    Hash map: 2 passes
    Time: O(n)
    Space: O(n)

    indices = {}
    for i, n in enumerate(nums):
        indices[n] = i

    for i, n in enumerate(num):
        diff = target - n
        if diff in indices and indices[diff] != i:
            return [i, indices[diff]]
    
    return []
    """

    """
    Hash map: 1 pass
    Time: O(n)
    Space: O(n)

    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []
    """

if __name__ == "__main__":
    main()