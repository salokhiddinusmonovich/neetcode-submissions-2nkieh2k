class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for index, num in enumerate(nums):
            a.append([num, index])
        a.sort()
        i, j  = 0, len(nums) - 1
        while i < j:
            cur = a[i][0] + a[j][0]
            if cur == target:
                return [min(a[i][1], a[j][1]), max(a[i][1], a[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []