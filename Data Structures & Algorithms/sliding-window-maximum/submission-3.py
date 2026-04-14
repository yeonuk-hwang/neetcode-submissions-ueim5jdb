class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        # k = 3
        # 0, 1, 2, / 1, 2, 3
        # left = right - length + 1
        for right in range(len(nums)):
            left = right - k + 1

            # if the first element in the queue is out of range, delete it from the queue
            if dq and dq[0] < left:
                dq.popleft()

            # if element in the queue is less than the current value, remove it
            # because it never be the max value
            # 1. it will be removed earlier than the current value (because current value is the later index)
            # 2. so, as the current value remains, the at least maximum value will be the current value

            current_num = nums[right]

            while dq and nums[dq[-1]] < current_num:
                dq.pop()
            
            dq.append(right)

            if right >= k - 1:
                result.append(nums[dq[0]])
            
        return result