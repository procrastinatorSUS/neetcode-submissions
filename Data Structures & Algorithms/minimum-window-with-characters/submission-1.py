from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        perm = Counter(t)
        mn = None
        l = r = 0
        while r <= (len(s)-1):
            while any(x > 0 for x in perm.values()) and r <= (len(s) - 1):
                if s[r] in perm:
                    perm[s[r]] -= 1
                r += 1
            while all(x <= 0 for x in perm.values()) and l <= (len(s) - 1):
                if mn is None or len(s[l:r]) < len(mn):
                    mn = s[l:r]

                if s[l] in perm:
                    perm[s[l]] += 1
                l += 1
        return mn if mn is not None else ''