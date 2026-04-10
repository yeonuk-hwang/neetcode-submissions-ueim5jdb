class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hash map {value: index}
        # iterate the array and find if the target - current value is in the hash map
        # if so, return the index, otherwise go the the next index

        map = {}

        for index, value in enumerate(nums):
            map[value] = index
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in map and map[diff] != index:
                return [index, map[diff]]

        return []
        