class Solution:
    def maxArea(self, heights: List[int]) -> int:
      # distance는 줄어들기만 한다, two pointers가 양쪽에서 좁혀온다면
      # height가 있고, 그 중에서 left 또는 right를 움직인다. 무슨 기준으로?
      # 둘 중 큰 height를 놔두고 작은 것을 움직이는 게 더 효율적이다, 왜냐면 height가 클 수록 area가 넓어지기에
      # 그런데 둘이 같다면?
      # 같다면, left, right 중 다음 숫자가 더 큰 쪽으로 움직이는 것이 맞나?

      left = 0
      right = len(heights) - 1
      max_area = 0

      while left < right:
        distance = right - left
        left_height = heights[left]
        right_height = heights[right]

        area = min(left_height, right_height) * distance
        max_area = max(area, max_area)

        print(left, right, left_height, right_height, area)

        if left_height > right_height:
            right -= 1
        elif right_height > left_height:
            left += 1
        elif left_height == right_height:
            next_left_value = heights[left + 1]
            next_right_value = heights[right - 1]

            if next_left_value >= right_height:
                left += 1
            else:
                right -= 1
        
      return max_area



      # [2, 7, 4, 5, 6, 7]
      # left = 0, right = 5, value = 2, 7, distance = 5, area = 10
      # left = 1, right = 5, value = 7, 7, distance = 4, area = 28

      # left = 2, right = 5, value = 4, 7, distance = 3, area = 12
      # left = 1, right = 4, value = 7, 6, distance = 3, area = 18

      # [2, 7, 4, 6, 6, 7]
      # left = 0, right = 5, value = 2, 7, distance = 5, area = 10
      # left = 1, right = 5, value = 7, 7, distance = 4, area = 28

      # left = 2, right = 5, value = 4, 7, distance = 3, area = 12
      # left = 1, right = 4, value = 7, 6, distance = 3, area = 18
