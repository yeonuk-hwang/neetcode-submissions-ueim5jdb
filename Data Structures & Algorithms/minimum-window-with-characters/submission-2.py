class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        t_counter = Counter(t)
        slide_counter = {}
        
        # 상태 추적용 변수 (all() 대신 사용)
        required = len(t_counter)
        formed = 0
        
        left = 0
        # 결과값은 (길이, 시작인덱스, 끝인덱스)만 저장
        ans = float("inf"), 0, 0

        for right in range(len(s)):
            # 1. 확장
            char = s[right]
            slide_counter[char] = slide_counter.get(char, 0) + 1
            
            # 공급이 수요를 딱 맞춘 순간
            if char in t_counter and slide_counter[char] == t_counter[char]:
                formed += 1

            # 2. 수축 (조건 만족 시)
            while formed == required:
                # 최단 길이 갱신 (슬라이싱 대신 인덱스만 기록)
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)

                removed_char = s[left]
                slide_counter[removed_char] -= 1
                
                # 공급이 수요 밑으로 떨어지는 순간
                if removed_char in t_counter and slide_counter[removed_char] < t_counter[removed_char]:
                    formed -= 1
                
                left += 1

        # 3. 마지막에 단 한 번만 슬라이싱
        return s[ans[1] : ans[2] + 1] if ans[0] != float("inf") else ""