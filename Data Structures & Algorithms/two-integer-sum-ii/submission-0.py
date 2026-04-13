class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start with left and right
        # if the sum is greater than target, decrease right
        # if the sum is less than target, increase the left

        left = 0
        right = len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]

            if two_sum == target:
                return [left + 1, right + 1]
            
            if two_sum > target:
                right -= 1

            if two_sum < target:
                left += 1