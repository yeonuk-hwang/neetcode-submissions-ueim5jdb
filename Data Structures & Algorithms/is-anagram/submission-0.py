class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}

        for character in s:
            chars[character] = chars.get(character, 0) + 1

        for character in t:
            chars[character] = chars.get(character, 0) - 1

        print(chars)
        
        return all(v == 0 for v in chars.values())