# 168. Excel Sheet Column Title
# Key: char values are reversed string of the remainders of the amount divided by 26,
# 'Z' appears to be as '01', if k equal 0 then the next m should be reduced by 1
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        str = ''
        m = columnNumber
        while m > 0:
            n = m // 26
            k = m - n * 26
            if k == 0:
                str = str + 'Z'
                n -= 1
            else:
                str = str + (chr(64 + k))
            m = n
        return str[::-1]

# m = 1
# m = 28 #'AB'
# m = 2147483647 #FXSHRXW
# m = 16380 #XEZ
# m = 16378 #XEX
# m = 16351 #XDW
# m = 7109 #JMK
# m = 7098 #JLZ
# m = 1 #A
# m = 25 #Y
m = 678 #ZB
# m = 26 #Z
print(Solution().convertToTitle(m))