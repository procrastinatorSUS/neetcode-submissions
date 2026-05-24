class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ko = k
        zxc = set(s)
        true_best = 0
        for char in zxc:
            k = ko
            l = r = best = cur = 0
            while r <= (len(s) - 1):
                if s[r] == char:
                    cur += 1
                    r += 1
                else:
                    if k != 0:
                        cur += 1
                        k -= 1
                        r += 1
                    else:
                        best = max(best, cur)
                        while s[l] == char:
                            l += 1
                            cur -= 1
                        else:
                            k += 1
                            l += 1
                            cur -= 1
            best = max(best, cur)
            true_best = max(true_best, best)
        return true_best