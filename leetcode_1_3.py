#two number sum Solution 1
import time
def twoSumv1(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    return [i,j]
start = time.time()
#res = twoSum([2,7,11,5],9)
end = time.time()
#print(end-start,res)


#two number sum Solution 2
def twoSumv2(nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]


#three sum Solution 1
def threeSum(nums):
    nums = sorted(nums)#sort list
    print(nums)
    res = []#result list
    le = len(nums)
    for i in range(le-2):#i used as pivot
        r = le-1 # r is the last element
        print(i,r)
        for l in range(i+1, le-1, 1):#l is the element to the right of i
            if l == r:
                break
            print(l)
            if l>r: #when l>r, i++
                continue
            v = nums[i]+nums[l]+nums[r]
            print([i,l,r],nums[i],nums[l],nums[r])
            while v > 0:#if sum > 0, this means that the r value needs to be smaller
                r-=1 # reduce r by one
                print(r,l)
                if r<=l: #if r <= l, break, otherwise may out of range or have duplicates
                    break
                v = nums[i]+nums[l]+nums[r]
                
                
            if v == 0: #append if sum == 0
                res.append([nums[i],nums[l],nums[r]])
                print('app')
            
                    
            
                
            
                
    res_tu = set(tuple([tuple(sorted(x)) for x in res]))#remove duplicate lists
    res = [list(x) for x in res_tu]
    print(sorted(res))
##threeSum([1,2,-2,-1,1])


#maximum binary tree
class Solution:
    def constructMaximumBinaryTree(nums):
        if nums == []: return None
        max_num = max(nums)#max num in current list
        max_index = nums.index(max_num)#index
        root = TreeNode(max_num)#construct a treenode class
        root.left = self.constructMaximumBinaryTree(nums[0 : max_index])#left recursive
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1 :])#right recursive
        return root

#3-D cubes surface area
def surfaceArea(grid):
    area = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]>0:
                area += grid[i][j]*4+2
            if i-1>=0 and grid[i-1][j]>0:
                area -= min(grid[i][j],grid[i-1][j])
            if j-1>=0 and grid[i][j-1]>0:
                area -= min(grid[i][j],grid[i][j-1])
            if i+1<n and grid[i+1][j]>0:
                area -= min(grid[i][j],grid[i+1][j])
            if j+1<n and grid[i][j+1]>0:
                area -= min(grid[i][j],grid[i][j+1])
                
    
    return area
#print(surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))

# max of the sum of elements in sub array
def maxSubArray(nums):
    tmp = nums[0]
    sum_n = 0
    for i in range(len(nums)):
        if sum_n <= 0:
            sum_n = nums[i]
        else:
            sum_n += nums[i]
        tmp = max(sum_n,tmp)
    return tmp
    
#print(maxSubArray([-1,3,2,-2,1,4,7]))

            
#reverse listnode
def reverseList(head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		# 申请两个节点，pre和 cur，pre指向None
		pre = None
		cur = head
		# 遍历链表，while循环里面的内容其实可以写成一行
		# 这里只做演示，就不搞那么骚气的写法了
		while cur:
			# 记录当前节点的下一个节点
			tmp = cur.next
			# 然后将当前节点指向pre
			cur.next = pre
			# pre和cur节点都前进一位
			pre = cur
			cur = tmp
		return pre	

