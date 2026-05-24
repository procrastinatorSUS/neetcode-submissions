class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = Counter(s1)
        l = r = 0
        while r <= (len(s2)-1):
            if s2[r] in perm:
                while perm[s2[r]] == 0:
                    if s2[l] in perm:
                        perm[s2[l]] += 1
                    l += 1
                perm[s2[r]] -= 1
            else:
                while l != r:
                    if s2[l] in perm:
                        perm[s2[l]] += 1
                    l += 1
            r += 1
            if not(any(perm.values())):
                return True
        return False