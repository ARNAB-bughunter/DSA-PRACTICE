class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 1
        for i in range(len(s)):
            temp = s[i]
            max_length = max(max_length, 1)
            for j in range(i + 1, len(s)):
                if s[j] in temp:
                    break
                temp += s[j]
                max_length = max(max_length, len(temp))
        return max_length
    
obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))