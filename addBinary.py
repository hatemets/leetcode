class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, a, b, carry = "", a[::-1], b[::-1], False

        for i in range(max(len(a), len(b)) + 1):
            ba, bb = 0 if i >= len(a) else int(a[i]), 0 if i >= len(b) else int(b[i])

            if ba + bb == 2:
                res += "1" if carry else "0"
                carry = True
            elif ba + bb == 1:
                res += "0" if carry else "1"
            else:
                res += "1" if carry else "0"
                carry = False

            # print(str(i) + ":", ba, bb, res[-1])

        if res[-1] == "0":
            res = res[:-1]

        return res[::-1]

# print(Solution().addBinary("11", "1"))
# print(Solution().addBinary("1010", "1011"))
# print(Solution().addBinary("11", "111"))
# print(Solution().addBinary("1100001001", "101000001"))
# print(Solution().addBinary("0", "0"))
