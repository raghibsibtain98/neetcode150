class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs :
            encoded += str(len(string)) + ';' + string

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        pointer = 0

        while(pointer<len(s)):
            tmp = pointer
            while s[tmp] != ';':
                tmp += 1
            len_of_encoded_part = int(s[pointer:tmp])
            decoded.append(str(s[tmp+1 : tmp+1+len_of_encoded_part]))
            pointer = tmp+1+len_of_encoded_part
        
        return decoded