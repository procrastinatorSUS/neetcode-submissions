class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {sym:s.count(sym) for sym in set(s)}
        dict_t = {sym:t.count(sym) for sym in set(t)}
        if dict_s != dict_t:
            return False
        else:
            for sym in dict_s:
                if dict_s[sym] != dict_t[sym]:
                    return False
        return True