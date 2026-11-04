class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_map = defaultdict(int)

        l,r = 0,0
        max_len = 0

        while(r<len(s)):
            if s[r] in character_map:
                l = max(character_map[s[r]]+1,l)

            character_map[s[r]] = r
            max_len = max((r-l+1),max_len)
            r+=1
                
        
        return max_len
