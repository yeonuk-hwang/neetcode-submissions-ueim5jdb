class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute-force method:
        # loop inside loop, to iterate all other elements except the current element
        
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                prefix[i] = 1
                continue
            
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = 1
                continue

            suffix[i] = suffix[i + 1] * nums[i + 1]

        res = []       
        for i in range(0, len(nums)):
            res.append(prefix[i] * suffix[i])

        return res