#最长回文串
def longestPalindrome_v1(s):#暴力搜索的动态规划版
    size = len(s)
    if size < 2:
        return s

    dp = [[False for _ in range(size)] for _ in range(size)]

    max_len = 1
    start = 0

    for i in range(size):
        dp[i][i] = True

    for j in range(1, size):
        for i in range(0, j):
            dp[i][j]=ifP(s[i:j+1])

            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    print(start,max_len,dp)
    return s[start:start + max_len]
def longestPalindrome_v1(s):#最长公共子串的动态规划版
def ifP(s):
    if len(s) == 0: return True
    if len(s)%2 == 0:
        if s[:len(s)//2] == s[::-1][:len(s)//2]:
            return True
        else:
            return False
    if len(s)%2 == 1:
        if s[:(len(s)-1)//2] == s[::-1][:(len(s)-1)//2]:
            return True
        else:
            return False


print(ifP("aba"),ifP("abca"),ifP("abc"),ifP("abba"),ifP("abc435cba"))
print(longestPalindrome_v1("cabac"))
