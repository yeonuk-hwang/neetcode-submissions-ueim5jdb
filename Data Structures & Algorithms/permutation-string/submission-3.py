class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get the length of s1
        # iterate s2 with fixed size sliding window
        # if the character count in sliding window is same as s1, then return true
        # if it reaches the end, return false

        s1_length = len(s1)
        count = Counter(s1) # O(s1)

        left = 0

        for right in range(left + s1_length, len(s2) + 1):
            window_count = Counter(s2[left:right])
            if window_count == count:
                return True
            left += 1

        return False
