class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        best = 0

        l = 0
        r = 0
        while r <= len(s) - 1:
            if s[r] not in cur:
                cur.add(s[r])
                r += 1
            else:
                best = max(best, len(cur))
                while s[r] in cur:
                    cur.remove(s[l])
                    l += 1
        best = max(best, len(cur))
        return best
