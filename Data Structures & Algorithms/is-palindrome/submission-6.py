class Solution:
    # with extra space
    # def isPalindrome(self, s: str) -> bool:
    #     new_s = ""
    #     for char in s:
    #         if char.isalnum():
    #             new_s += char.lower()
        
    #     return new_s == new_s[::-1]

    # without extra space   
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while (i < j):
            while (i<j and not s[i].isalnum()) :
                i += 1

            while (i<j and not s[j].isalnum()) :
                j -= 1

            if s[i].lower() == s[j].lower() :
                i+=1; j-=1
                continue
            return False

        return True