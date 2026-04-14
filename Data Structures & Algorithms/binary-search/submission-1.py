class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = left + ((right - left) // 2)

            print("m", m)
            print("left", left)
            print("right", right)
            print("m_val", nums[m])

            if nums[m] == target:
                return m
            if target > nums[m]:
                left = m + 1
            if target < nums[m]:
                right = m - 1
            
        return -1 
