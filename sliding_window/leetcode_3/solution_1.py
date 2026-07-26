class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if len(set(s[i:j])) == len(s[i:j]):
                    max_lenght = max(max_lenght, j - i)
        return max_lenght      



obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))