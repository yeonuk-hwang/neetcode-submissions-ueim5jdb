class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialise counter with s1
        # initialise counter with s2, sliced from 0 to s1 length

        # compare them, if they are identical, return True

        # move fixed size window
        # left = 0, right = s1 length - 1 is already counted
        # move the right pointer to the next, left is right - s1_length + 1
        # removed pointer is right - s1_length, remove the character from the counter,
        # add the new right character to the counter
        # compare them, and return result
            # for example, if s1 length is 3
            # left = 0, right = 2 -> initial point
            # left = 1, right = 3 -> first movement
            # removed left = right - s1 length, left = right - s1 length + 1
        # 

        s1_len = len(s1)
        s1_counter = Counter(s1)
        window_counter = Counter(s2[:s1_len])

        if s1_counter == window_counter:
            return True
        

        for right in range(s1_len, len(s2)):
            appended_char = s2[right]
            removed_char = s2[right - s1_len]

            if window_counter[removed_char] == 1:
                del window_counter[removed_char]
            else:
                window_counter[removed_char] -= 1
            
            window_counter[appended_char] += 1

            if s1_counter == window_counter:
                return True

            

        return False


