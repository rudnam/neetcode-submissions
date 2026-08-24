class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashArr = {}

        # Count characters in s
        for i in s:
            if i in hashArr:
                hashArr[i] += 1
            else:
                hashArr[i] = 1
        
        print(hashArr)

        # Count characters in t
        for j in t:
            if j in hashArr and hashArr[j] >= 1:
                hashArr[j] -= 1
            else:
                return False

        return True             