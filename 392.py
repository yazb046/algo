# 392. Is Subsequence
# Key: Split t by s elements and analyze remainder
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        nStr = t
        for ss in s:
            if len(nStr) == 0:
                return False
            if ss in nStr:
                index  = nStr.index(ss)
                nStr = nStr[index + 1:]
            else:
                return False
        return True

# print(Solution().isSubsequence("abc", "ahbgdc"))
# print(Solution().isSubsequence("axc", "ahbgdc"))
# print(Solution().isSubsequence("ab", "baab"))
print(Solution().isSubsequence("aaaaaa", "bbaaaa"))