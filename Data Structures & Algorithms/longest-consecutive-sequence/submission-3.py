class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # lookup the next consecutive element -> using hash?
        # 그런데, 만약 다음 숫자가 없다면 어떻게 그 다음 최소값을 찾아내지?
        # convert array to the hash set - O(n)

        # only if n - 1 is not in the set, the value can be start of the sequence
        # iterate the value and find the start value array - O(n)

        # iterate the start array 
        # count consecutive sequence using hash set starting from start array

        hash_set = set(nums) # O(n)
        start_nums = list()

        for num in nums:
            if not (num - 1 in hash_set):
                start_nums.append(num)

        max_sequence = 0

        for start in start_nums:
            sequence = 1
            current_num = start
            
            while current_num + 1 in hash_set:
                sequence += 1
                current_num += 1

            if sequence > max_sequence:
                max_sequence = sequence

        return max_sequence
