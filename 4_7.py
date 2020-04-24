#机器人能到达的矩阵中的格子
#BFS
#维持一个队列，将(0,0)推入，每推入一次，ans+=1
#维持一个集合visited，保存到达过的位置
#当队列为空时，结束并返回
#每次推出一个位置，判断临近位置中可到达的位置，并推入队列
#将推出的位置加入visited。

def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited,  = [(0, 0, 0, 0)], set()#设置队列和集合
        while queue:#当队列为空时结束
            i, j, si, sj = queue.pop(0)#堆出位置，si,sj为各个位数的和(11:1+1=2)
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or \
            (i, j) in visited: continue#当此位置不符合条件，即不可到达的位置时countinue
            visited.add((i,j))#如可到达，加入visited
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))#放入周围的位置
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)#返回到过的位置的数量

#DFS
#使用递归，每次递的时候向下和向右，状态为位置
#当不满足条件时返回0，即无法到达，
#return 1+向下+向右,因此先向下直到无法到达，再返回上一层执行向右，当一层的下和右都执行完成，返回上一层
def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

#无重复字符的最长子串
#滑动窗口，如果当前子串S(i,j-1)不重复，只需检查S[j]是否重复，使用一个列表保存窗口
#遍历S，当前char如果不在列表中，append，如果当前列表长度大于max_l，更新max_l。
#如果已经在列表中，先append，再将列表中重复的char
#的位置之前的元素全部移除，继续遍历。因为移除后的列表长度一定小于等于移除之前的，所以不必更新max_l。
def lengthOfLongestSubstring(s):
    l = len(s)
    if l == 0:
        return 0
    max_l = 1#对于一个长度大于等于1的子串来说，最小的无重复最长子串为1
    store = []#建立列表
    for i in range(l):#遍历S
        if s[i] not in store:#当前元素不在列表中，意味着不重复
            store.append(s[i])#append
            if len(store) > max_l:#当前列表长度大于max_l的话
                max_l = len(store)#更新
        else:#有重复
            store.append(s[i])#先放入重复的元素
            index = store.index(s[i])#获取第一个重复元素的index
            store = store[index+1:]#移除包括那个index之前的所有元素
    return max_l#返回max_l
print(lengthOfLongestSubstring("nfpdmpi"))
    
        
            
            
