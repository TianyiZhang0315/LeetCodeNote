#反转链表
#递归
#判断归的条件为下一个节点为空，则返回当前节点
#或当前节点为空，对应特殊例子，只有一个空节点
#每一层归的目标，当前节点和下一节点的关系，由指向下一节点
#变为下一节点指向自己 1->2变为1<-2
#再将当前节点next设为none，在链表中间的节点其实没有必要，但是方便把开头节点指向none（None<-1）
def reverseList(self, head: ListNode) -> ListNode:
        # 归
        if head == None or head.next == None: return head
        # 递
        p = self.reverseList(head.next)
        # 交换当前head 和 head.next
        head.next.next = head
        head.next = None
        return p

#2两数相加
#迭代
def addTwoNumbers(self, l1, l2):
        # 定义一个进位标志
        a,b,p,carry = l1,l2,None,0
        while a or b:
                # a和b节点的值相加，如果有进位还要加上进位的值
                val = (a.val if a else 0)+(b.val if b else 0)+carry
                # 根据val判断是否有进位,不管有没有进位，val都应该小于10
                carry,val = val/10 if val>=10 else 0,val%10
                p,p.val = a if a else b,val
                # a和b指针都前进一位
                a,b = a.next if a else None,b.next if b else None
                # 根据a和b是否为空，p指针也前进一位
                p.next = a if a else b
        # 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件	
        if carry:
                p.next = ListNode(carry)
        # 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1	
        return l1

#递归
#不同于反转链表，每一层操作在向深层递的过程中完成，每一层返回自己的node
#这样最后一层返回的是l1的第一个node
#每一次计算后更改l1的值，并且传递carry给下一层
#当l1,l2长短不同时，当某一层一方为None而另一方不为None，将ListNode(0)赋予那个node
#这样可以实现在l1总是返回最长的链表，每次递归函数的返回值赋给l1.next确保将新创建
#的node相连
#总结：向下传递时的工作为计算并更新，传递carry
#向上返回时的工作将当前node与下层返回的node相连，并返回当前node给上层
def addTwoNumbers(self, l1, l2):
		# 主要逻辑都在内部函数中实现
		def add(a,b,carry):
			# 递归的终止条件是a和b都为空
			# 如果carry大于0需要返回一个进位标志
			if not (a or b):
				return ListNode(1) if carry else None
			# 如果a为空则将ListNode(0)赋给a，对于b也是
			a = a if a else ListNode(0)
			b = b if b else ListNode(0)
			#处理val，以及进位标志
			val = a.val + b.val + carry
			carry = 1 if val>=10 else 0
			a.val = val%10
			# 现在a的值就是两个节点相加后的和了
			# 之后再次递归计算a.next和b.next
			a.next = add(a.next,b.next,carry)
			return a
		return add(l1,l2,0)

