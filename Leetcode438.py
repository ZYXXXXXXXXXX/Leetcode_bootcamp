class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        exp = {}
        if len(p) > len(s):
            return []

        for items in p:
            if items in exp:
                exp[items] += 1
            else:
                exp[items] = 1
        dic = {}
        res = []
        for i in range(len(p)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1

        for start in range(len(p), len(s)):
            if dic == exp:
                res.append(start - len(p))

            if s[start - len(p)] in dic and dic[s[start - len(p)]] > 1:
                dic[s[start - len(p)]] -= 1
            else:
                del dic[s[start - len(p)]]

            if s[start] in dic:
                dic[s[start]] += 1
            else:
                dic[s[start]] = 1

        if dic == exp:
            res.append(len(s) - len(p))
        return res
