#24 points

def judgePoint24(nums):
    if not nums: # return false if empty num
        return False
    def helper(nums): # helper function for recursive use
        if len(nums) == 1: # if only one element in nums, check if equals to 24
            return abs(nums[0]-24)<1e-6
        for i in range(len(nums)): # iterate through nums
            for j in range(len(nums)):
                if i != j: # i and j have to be different
                    new = [nums[k] for k in range(len(nums)) if i!=k!=j] # new is the list contains elements other than index i and j
                    if helper(new+[nums[i]+nums[j]]): # recursive step for operator plus
                        return True
                    if helper(new+[nums[i]-nums[j]]): # recursive step for operator minus
                        return True
                    if helper(new+[nums[i]*nums[j]]): # recursive step for operator mul
                        return True
                    if nums[j] != 0 and helper(new+[nums[i]/nums[j]]): # recursive step for operator plus(no 0 division)
                        return True #这里要返回True的话， 递归的最后一层到这一层之间都要返回True才能实现。
        return False # if none of above is satisfied 
    return helper(nums)



#symmetric binary tree (note: every child tree is symmetric)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# method 1 (recursive)
def isSymmetric_v1(self, root: TreeNode) -> bool:
    if not root: # symmetric if only root exists
        return True
    def dfs(left, right): # recursive function
        # stop conditions: both none, one is none, left != right.
        if not (left or right): # stop condition (both left and right are None)
            return True # symmetric
        if not (left and right): # stop condition (one is None and the other one is not None)
            return False # asymmetric
        if left != right: # stop condition (left != right)
            return False # asymmetric
        return dfs(left.left, right.right) and dfs(left.right, right.left) # recursively check if child tree nodes also symmetric
    return dfs(root.left,root.right)
    
# method 2 (queue)
def isSymmetric_v2(self, root: TreeNode) -> bool:
    if not root or not (root.left or root.right): # check root and left and right (symmetric)
        return True
    queue = [root.left, root.right] # initiate queue
    while queue: 
        left = queue.pop(0)# pop left and right from queue
        right = queue.pop(0)
        if not (left or right): # check conditions (same as in recursive)
            continue
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        queue.append(left.left)# append child nodes into queue
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    return True # symmetric if queue is empty at the end (did not trigger stop condition)
