class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for item in strs:
            result += str(len(item))
            result += "#"
            result += item

        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        # 012 345678910 11 12
        # 10# abcdefg h i  j

        while left < len(s):
            right = left # 0

            while s[right] != "#": #0, 1, 2
                right += 1

            length = int(s[left:right])

            left = right + 1
            right = right + length # 12

            res.append(s[left:right + 1])
            left = right + 1

        print(res)

        return res