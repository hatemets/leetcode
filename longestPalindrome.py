class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm: dict[str, int] = { ch: s.count(ch) for ch in set(s) }

        if (len(hm.values()) == 1):
            return list(hm.values())[0]

        hasSingles = 1 in hm.values()

        res: int = 1 if hasSingles else 0

        oddUsed: bool = hasSingles
        for value in hm.values():
            if value > 1:
                if not oddUsed and value % 2 == 1:
                    res += value
                    oddUsed = True
                else:
                    res += int(value / 2) * 2

        return res

print(Solution().longestPalindrome("ababababa"))
