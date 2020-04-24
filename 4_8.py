#括号生成
#暴力枚举，生成所有可能的序列，然后判断是否合法
#遍历一个序列，当右括号数量严格大于左括号数量时，这个序列不合法，例:())

#DFS
#暴力枚举的升级版，当右括号数量比左括号多时，剪枝
def generateParenthesis_dfs(n):

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0: #当左右括号全部用完，加入列表
                res.append(cur_str)
                return
            if right < left:#如果右边括号比左边多，剪枝，返回
                return
            if left > 0:#如果左边括号有剩余，放置一个左括号
                dfs(cur_str + '(', left - 1, right)
            if right > 0:#如果右边括号有剩余，放置一个右括号
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res
#print(generateParenthesis_dfs(3))

#BFS
#通过编写广度优先遍历的代码，读者可以体会一下，为什么搜索几乎都是用深度优先遍历（回溯算法）。

#广度优先遍历，得程序员自己编写结点类，显示使用队列这个数据结构。
#深度优先遍历的时候，就可以直接使用系统栈，在递归方法执行完成的时候，系统栈顶就把我们所需要的状态信息直接弹出，而无须编写结点类和显示使用栈。


#动态规划
#原理为任意n的状态下,n+1对括号可以表示为(a)b,且a+b = n，a和b为合法的括号序列
#例:当n = 3时，可以表示为(0)2,或(1)1或(2)0,又因n = 2的合法括号序列有两种()()和(())，
#n = 3最终解为五种
#在这里任意n的括号序列只依赖于括号数量小于n的序列
def generateParenthesis_dynamic(n):
    if n == 0:#当n=0
        return []

    dp = [None for _ in range(n + 1)]
    dp[0] = [""]#初始化状态矩阵

    for i in range(1, n + 1):#i为总的括号序列的括号个数
        cur = []
        for j in range(i):#j为第一个括号序列的括号个数
            left = dp[j]#(left)right
            right = dp[i - j - 1]
            for s1 in left:#遍历两种括号序列的可能性
                for s2 in right:
                    cur.append("(" + s1 + ")" + s2)#生成新的当前n=i+1的括号序列
        dp[i] = cur#将所有可能放入状态矩阵
    return dp[n]#返回第n个

#不同的二叉搜索树
#任意子树根节点的值要大于左子树的值，且小于右子树的值
#动态规划，三维dp矩阵，dp[i][j]代表从i到j的可能的二叉搜索树
#通过遍历1到j,作为根节点，将i到j切分成dp[1][i-1]和dp[i+1][j]进行排列组合，前者为左，后者为右
def generateTrees(n):#none type报错
        if n == 0:
            return None
        # 对dp进行初始化
        dp = []
        for i in range(0, n+1):   # 初始化dp
            dp.append([])
            for j in range(0, n+1):
                if i == j:
                    dp[i].append([TreeNode(i)])
                elif i < j:
                    dp[i].append([])
                else:
                    dp[i].append([None])
        dp[0][0] = [None]
        for i in range(n-1, 0, -1):  # 自下向上进行循环
            for j in range(i+1, n+1):
                for r in range(i, j+1):   # i-j每一个节点为顶点的情况
                    left = r+1 if r < j else r    # 右边的值需要边界判断，不然会溢出数组
                    for x in dp[i][r-1]:          # 左右子树排列组合   
                        for y in dp[left][j]:
                            node = TreeNode(r)     
                            node.left = x
                            node.right = y
                            if r == j:
                                node.right = None
                            dp[i][j].append(node)      # dp[i][j]添加此次循环的值
        return dp[1][n]

#递归，逻辑与动态规划相似
#若n=0,返回[]
#定义递归的函数，如果左边界left大于右边界right则返回[None]
#遍历range(left,right+1),得到左右子树，遍历左右子树，与当前根节点结合，添加到列表中
#遍历结束后返回列表
def generateTrees_re(n):
    if(n==0):#特例n=0
        return []
    def build_Trees(left,right):#递归函数
        all_trees=[]#储存当前状态所有可能结果的列表
        if(left>right):#左大于右，不合法
            return [None]
        for i in range(left,right+1):#遍历所有可能点作为根节点
            left_trees=build_Trees(left,i-1)#得到左右子树
            right_trees=build_Trees(i+1,right)
            for l in left_trees:#遍历左右子树
                for r in right_trees:
                    cur_tree=TreeNode(i)#设置根节点
                    cur_tree.left=l#设置左右子树
                    cur_tree.right=r
                    all_trees.append(cur_tree)#添加到结果列表
        return all_trees#返回结果列表
    res=build_Trees(1,n)#开始递归函数
    return res
