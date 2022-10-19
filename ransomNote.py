class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm: dict[str, int] = { ch: magazine.count(ch) for ch in set(magazine) }

        for ch in ransomNote:
            if hm.get(ch) and hm[ch] > 0:
                hm[ch] -= 1
            else:
                return False

        return True


# print(Solution().canConstruct("givethemoney", "thisistodaysweatherforecastsoitsgonbesunnyandoverallaniceday"))
print(Solution().canConstruct("john", "hnjokolocojakey"))
