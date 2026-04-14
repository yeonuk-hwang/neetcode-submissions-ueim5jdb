class Solution:
    def is_numbers(self, val:str):
        try:
            int(val)
            return True
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []


        for token in tokens:
            if self.is_numbers(token):
                num_stack.append(token)
            else:
                back = num_stack.pop()
                front = num_stack.pop()
                result = eval(f"{front} {token} {back}")
                num_stack.append(int(result))
                print(front, token, back)
                print(result)
        
        return int(num_stack.pop())