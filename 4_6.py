#最长回文
#动态规划，如果一个子串S[i+1,j-1]是回文，当S[i]=S[j]时，S[i,j]也一定是回文
#让j从1到size-1,i从0到j-1遍历所有子串并把长度存储在size^2的表格中。
def longestP(s):
    
    size = len(s)
    dp = [[0 for _ in range(size)] for _ in range(size)]
    
    if size < 2:
        return size
    max_l = 1
    start = 0
    for i in range(size):
        dp[i][i] = 1
    for j in range(1,size):
        for i in range(0,j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = j-i+1
                else:
                    if dp[i+1][j-1] > 0:
                        dp[i][j] = dp[i+1][j-1]+2
            else:
                dp[i][j] = 0
            if dp[i][j] > max_l:
                max_l = dp[i][j]
                start = i
    print(max_l,start,dp)
    return s[start:start+max_l]
                
                
#print(longestP("abcda"))
#中心扩散法
#以一个字符（奇数长度）或两个字符的间隔（偶数长度）为中心，向两端扩散
#直到不满足回文条件或左右一边到达边界，返回子串和长度
#每次遍历记录最大长度和对应子串
def longestPalindrome(s):
        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = center_spread(s, size, i, i)
            palindrome_even, even_len = center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

def center_spread(s, size, left, right):
    """
    left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
    right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
    """
    i = left
    j = right

    while i >= 0 and j < size and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1:j], j - i - 1

#面试题01.07
#矩阵原地旋转，先用切片实现上下反转，再用遍历实现对角线反转。
#切片为浅复制，原变量改变嵌套的列表内的值时，新变量的嵌套内列表也会改变
#深复制则全部不改变,list[:]=list[::-1]相当于在list本身做改变，id是一样的
def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = matrix[::-1]
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
##l = [1,2,3,[4,5],7]
##print(id(l))
##def test(l):
##    print(id(l))
##    l[:] = l[::-1]
##    print(id(l))
##    l[1],l[0] = l[0],l[1]
##    print(l,"1")
##test(l)
##print(l,"2")
    
