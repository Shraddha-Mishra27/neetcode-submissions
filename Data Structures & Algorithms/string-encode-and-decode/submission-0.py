class Solution:

    def encode(self, strs):
        ans = ""
        
        for s in strs:
            ans += str(len(s)) + "#" + s
        
        return ans

    def decode(self, s):
        ans = []
        i = 0
        
        while i < len(s):
            j = i
            
            # length find karo
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            # actual string
            word = s[j + 1 : j + 1 + length]
            ans.append(word)
            
            # next string par jao
            i = j + 1 + length
        
        return ans