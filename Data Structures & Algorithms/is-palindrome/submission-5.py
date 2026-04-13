class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using two pointers
        # move left until it indicates alnum char (start from 0)
        # move right until it indicates alnum char (start from len - 1)
        # compare them
        # if both of the is not identical -> return False
        # if both of them is identical ->
        #  increase left pointer by 1 and decrease right pointer by 1

        left = 0
        right = len(s) - 1

        while left < right:
            print(left, right)
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and right > left:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right -=1
            
        return True