class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # push to the stack, if stack is empty 
        # or the top element is not warmer than the current temperature

        # if the current temperature is warmer than the top
        # pop the top element (index), and calculate the waiting day by current index - top index
        # iterate until the current temperature is not warmer than the top


        result = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                target_index = stack.pop()
                result[target_index] = index - target_index
            
            stack.append(index)

        return result
            

                    
        