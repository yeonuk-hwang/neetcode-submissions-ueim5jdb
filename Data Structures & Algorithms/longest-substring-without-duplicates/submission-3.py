class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        max_sequence = 0

        # 0, 0에서 시작한다
        # right값에 있는 것이 seen에 있다면 left를 증가시켜서 windows의 크기를 줄인다.
        # right값에 있는 것을 seen에 {char: index} 형태로 추가한다.

        for right in range(len(s)):
            character = s[right]

            # character가 seen에 있다. 다만 seen은 현재까지 나온 모든 char을 추가하기 때문에
            # 현재 window안에 character가 있는지를 검증해야 한다.
            # 그 말은 현재 윈도우인 left <= index <= right 안에 있는 값인지 봐야 한다는 뜼
            # seen[character]는 어차피 right보다 클 수 없기에, 후자의 조건은 만족된다.
            # 만약 현재 윈도우 안에 있다면 해당 글자보다 한칸 앞으로 window의 시작점을 조정해야 한다.
            # 그것이 중복이 없는 최대 length이기 때문이다.

            if character in seen and seen[character] >= left:
                left = seen[character] + 1
            
            seen[character] = right
            max_sequence = max(max_sequence, right - left + 1)
            
        return max_sequence
            
