class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = hours you have to eat all the bananas
        # piles = the number of bananas

        # k = bananas per hour eating rate 
        # each time per pile = pile / k
        # total time = sum of each time

        # maximum k = max(piles)
        # minimum k = 1

        # 만약 가능하다면, k를 낮출 수 있는지 찾기
        # 만약 불가능하다면, k를 늘리기
        # 1 - max(piles) 사이에서, total_time <= h를 만족하는 최소값 찾기

        left = 1
        right = max(piles)

        result = right

        while left <= right:
            middle = left + ((right - left) // 2)

            print(left, right, middle)
            total_hours = sum([math.ceil(pile / middle) for pile in piles])
            print(total_hours)

            if h >= total_hours:
                result = middle
                right = middle - 1
            elif h < total_hours:
                left = middle + 1

        return result
                



