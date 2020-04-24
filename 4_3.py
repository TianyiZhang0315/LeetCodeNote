#42接雨水
def trap(height):#解法超时
    length = len(height)
    if length == 0:
        return 0
    d = 0
    for n in range(max(height)):
        q = 0
        #print(n,d)
        for i in range(1,length):
            #print(n,q)
            if height[i] == 0:
                #print("iter %d is 0"%i)
                if height[i-1] > 0 and q == 0:
                    q += 1
                    height[i-1] -= 1
                    continue
                if q > 0 and height[i-1] == 0:
                    q += 1
            else:
                #print("iter %d is not 0"%i)
                if i == length - 1:
                    if height[i-1] == 0 and q > 0:
                        d += q
                        #print(n,i,d)
                        q = 0
                        height[i] -= 1
                        continue
                    if height[i-1] > 0:
                        height[i-1] -= 1
                        height[i] -= 1
                else:
                    if height[i-1] == 0 and q > 0:
                        d += q
                        #print(n,i,d)
                        q = 0
                        continue
                    if height[i-1] > 0:
                        height[i-1] -= 1
    return d
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
#双指针
def trap_pointer(self, height):
        # 边界条件
        if not height: return 0
        n = len(height)

        left,right = 0, n - 1  # 分别位于输入数组的两端
        maxleft,maxright = height[0],height[n - 1]
        ans = 0

        while left <= right:
            maxleft = max(height[left],maxleft)
            maxright = max(height[right],maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1

        return ans
#使用栈
#https://leetcode-cn.com/problems/trapping-rain-water/solution/dan-diao-zhan-jie-jue-jie-yu-shui-wen-ti-by-sweeti/
def trap_stack(self, height: List[int]) -> int:
        length=len(height)
        if length<3:return 0
        res,idx=0,0
        stack=[]
        while idx<length:
            while len(stack)>0 and height[idx]>height[stack[-1]]:
                top=stack.pop()#index of the last element in the stack
                if len(stack)==0:
                    break
                h=min(height[stack[-1]],height[idx])-height[top]
                dist=idx-stack[-1]-1
                res+=(dist*h)
            stack.append(idx)
            idx+=1 
        return res
#动态编程
#从左向右遍历出height长度的最大值列表，从右向左做同样
#每个index位置的蓄水为两者的交集减去当前index的height值，即min(leftmax[i],rightmax[i])-height[i]
def trap_dynamic(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        ans = 0
        # 初始化
        maxleft[0] = height[0]
        maxright[n-1] = height[n-1]
        # 设置备忘录，分别存储左边和右边最高的柱子高度
        for i in range(1,n):
            maxleft[i] = max(height[i],maxleft[i-1])
        for j in range(n-2,-1,-1):
            maxright[j] = max(height[j],maxright[j+1])
        # 一趟遍历，比较每个位置可以存储多少水
        for i in range(n):
            if min(maxleft[i],maxright[i]) > height[i]:
                ans += min(maxleft[i],maxright[i]) - height[i]
        return ans

                    
            
        
