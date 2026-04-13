class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        fr = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            fr[cnt].append(num)
        
        res = []
        for i in range(len(fr) - 1, 0, -1):
            for j in fr[i]:
                res.append(j)
                if len(res) == k:
                    return res