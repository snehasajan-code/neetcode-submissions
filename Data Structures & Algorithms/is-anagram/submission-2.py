from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_map=Counter(s)
        t_map=Counter(t)

        for letter in s_map:
            if s_map[letter]!=t_map[letter]:
                return False
        
        for letter in t_map:
            if s_map[letter]!=t_map[letter]:
                return False
        
        return True
        
        