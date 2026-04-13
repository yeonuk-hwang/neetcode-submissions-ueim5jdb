class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a stack and push the characters if it is alphanumeric
        # iterate the char again and compare them with stack.pop
        # it checks if the current character is same as the last character in the stack

        stack = []

        for char in s:
            if char.isalnum():
                stack.append(char.lower())
        
        for char in s:
            if char.isalnum():
                if char.lower() != stack.pop():
                    return False

        return True
