class Solution:
    def trap(self, height: List[int]) -> int:
        # 왼쪽이랑 오른쪽 벽 중 가장 낮은 벽의 높이까지 물이 찰 수 있다.
        # 왼쪽벽이랑 오른쪽벽 중 가장 높은 벽을 찾는다.
        # 왼쪽이랑 오른쪽 중 낮은 쪽을 앞으로 더 이동한다.
        # trapped에 더한다

        # left = 0
        # right = 9
        
        # max_left = 0, max_right = 1

        # left = 1, right = 9
        # current left height = 2, max_left = 0, max_right = 1
        # current left height > max_left, max_right
        # max_left = 2, max_right = 1

        # left = 1, right = 8
        # current_right_height = 2, max_left = 2, max_right = 1
        # current right height > max_left, max_right
        # max_left = 2, max_right = 2

        # left = 2, right = 8
        # current_left_height = 0, max_left = 2, max_right = 2
        # max - current_left_height = 2
        # plus 2
        # left += 1

        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        result = 0

        while left < right:
            print("left", left)
            print("height[left]",height[left])
            print("right", right)
            print("height[right]",height[right])

            if height[left] < height[right]:
                left += 1
                current_height = height[left]
                print("current_height", current_height)
                max_left = max(max_left, current_height)
                print("max_left", max_left)
                min_pillar = min(max_left, max_right)
                print("min_pillar", min_pillar)
                if current_height < min_pillar:
                    result += min_pillar - current_height
                    print("result", result)
            else:
                right -= 1
                current_height = height[right]
                print("current_height", current_height)
                max_right = max(max_right, current_height)
                print("max_right", max_right)
                min_pillar = min(max_left, max_right)
                print("min_pillar", min_pillar)
                if current_height < min_pillar:
                    result += min_pillar - current_height
                    print("result", max_right)

        return result