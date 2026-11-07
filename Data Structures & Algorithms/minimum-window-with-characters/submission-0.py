class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map = defaultdict(int)
        for char in t:
            char_map[char]+=1
        
        r,l = 0,0
        count = 0
        t_len = len(t)
        min_len = float('inf')
        start_ind = -1

        while(r<len(s)):
            if s[r] in char_map and char_map[s[r]]>0:
                count += 1

            char_map[s[r]] -= 1

            while (count==t_len):
                if (r-l+1<min_len):
                    min_len = r-l+1
                    start_ind = l

                char_map[s[l]]+=1

                if char_map[s[l]]>0:
                    count-=1
                l+=1
            
            r+=1

        return s[start_ind:start_ind + min_len] if start_ind != -1 else ""

                



