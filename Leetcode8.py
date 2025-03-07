class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        while start < len(s) and s[start] == " ":
            start += 1

        if start >= len(s):
            return 0

        isPositive = True
        if s[start].isnumeric():
            isPositive = True
            start -= 1
        elif s[start] == "+":
            isPositive = True
        elif s[start] == "-":
            isPositive = False
        else:
            return 0
        start += 1

        res = ""
        while start < len(s) and s[start].isnumeric():
            res += s[start]
            start += 1
        if len(res) == 0:
            return 0
        res = int(res)
        if not isPositive:
            res = -res
        if res < -(2**31):
            res = -(2**31)
        if res > 2**31 - 1:
            res = 2**31 - 1
        return res
