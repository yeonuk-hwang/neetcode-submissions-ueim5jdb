class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        middle = len(s) // 2
        stack = []
        table = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for parenthese in s:
            if parenthese in table:
                stack.append(parenthese)
            else:
                if len(stack) == 0:
                    return False

                pair = stack.pop()
                if table.get(pair) != parenthese:
                    return False


        return len(stack) == 0