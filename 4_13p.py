#岛屿数量
##使用DFS, 用一个grid同样大小，类型为bool的二维矩阵记录位置是否被标记过
##过程为遍历每个位置，当前位置如果未越界，未被标记，并且为陆地则count+1并开始递归dfs
##遍历四个方向上的其他位置，如果其他位置未越界，未被标记，并且为陆地则递归dfs
##当遇到周围不再有未越界，未被标记，并且为陆地的位置，则结束递归，无返回变量
def numIslands(grid):
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    count += 1
                    __dfs(grid, i, j, m, n, marked)
                    # 【位置 1】
        return count

def __dfs(grid, i, j, m, n, marked):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    marked[i][j] = True
    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]
        if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
            __dfs(grid, new_i, new_j, m, n, marked)
a = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(a))
