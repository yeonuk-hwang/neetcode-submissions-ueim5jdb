class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 단조성을 띄는가?
        # OUZ가 만족 못 한다면 그 이하는 절대 만족 못 함
        # YXA가 만족 못 한다
        # YXAZ는 만족한다.
        # XAZV는 만족 못 한다.
        # 만족하는 순간, 현재의 길이를 저장한다.
        # left를 늘려서 다시 검사한다.
        # 만족 못 한다면 다시 right를 늘린다.

        s_len = len(s)
        t_len = len(t)

        if t_len > s_len:
            return ""

        left = 0
        right = 0

        t_counter = Counter(t)

        slide_counter = Counter(s[:t_len])

        if t_counter == slide_counter:
            return s[:t_len]

        current_substring = ""

        for right in range(t_len, len(s)):
            substring_len = right - left + 1

            appended_char = s[right]

            slide_counter[appended_char] += 1
            
            is_included = all([slide_counter[char] >= t_counter[char] for char in t_counter])

            while is_included:
                # save current window substring
                sub_string = s[left:right + 1]

                if current_substring == "":
                    current_substring = sub_string

                current_substring = current_substring if len(current_substring) < len(sub_string) else sub_string 

                # move left pointer to one point right
                removed_char = s[left]
                slide_counter[removed_char] -= 1
                is_included = all([slide_counter[char] >= t_counter[char] for char in t_counter])
                left += 1
                    


        return current_substring