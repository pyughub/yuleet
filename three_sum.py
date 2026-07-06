def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        ni = nums[i]
        if ni > 0:
            break
        if i and ni == nums[i - 1]:
            continue
        if ni + nums[i + 1] + nums[i + 2] > 0:
            break
        if ni + nums[n - 1] + nums[n - 2] < 0:
            continue
        j, k = i + 1, n - 1
        while j < k:
            s = ni + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                res.append([ni, nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return res


# O(n^3) — md spec: outer two pointers + scan k
def threeSum_md(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    i = 0
    j = len(nums) - 1
    three_sum = []

    while i < j:
        s = nums[i] + nums[j]
        for k in range(len(nums)):
            if k == i or k == j:
                continue
            if -s == nums[k]:
                three_sum.append([nums[i], nums[j], nums[k]])
        if s > 0:
            j -= 1
        else:
            i += 1

    seen = set()
    result = []
    for triplet in three_sum:
        key = tuple(sorted(triplet))
        if key not in seen:
            seen.add(key)
            result.append(list(key))
    return result


# alias of threeSum (sort + fix i + two pointers)
def threeSum_two_pointer(self, nums: list[int]) -> list[list[int]]:
    return threeSum(self, nums)
