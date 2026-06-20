class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        for i, num in enumerate(nums):
            my_list.append([num, i])
        my_list.sort()
        i, j  = 0, len(nums) - 1 
        while i < j:
            cur = my_list[i][0] + my_list[j][0]
            if cur == target:
                return [ min(my_list[i][1], my_list[j][1]), max(my_list[i][1], my_list[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []     