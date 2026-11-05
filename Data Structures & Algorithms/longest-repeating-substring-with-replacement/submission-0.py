class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left, right = 0,0
        letters = defaultdict(int)
        max_freq = 0
        while (right<len(s)):
            letters[ord(s[right])-ord('A')]+=1
            max_freq = max(max_freq,letters[ord(s[right])-ord('A')])
            if ((right-left+1)-max_freq > k):
                letters[ord(s[left])-ord('A')]-=1
                left+=1
            if ((right-left+1) - max_freq <=k):
                max_len = max(max_len,(right-left+1))
            right += 1

        return max_len          

