//今天复习链表
class node{//定义节点，含有val值和下个节点
    public int val;
    public node next;
    public node(int v){
        val = v;
        next = null;
    }
}
public class MyLinkedList {
    public node head;//这里的head其实是不变的，永远指向初始化的node（0）
    public int size;//链表长度
    /** Initialize your data structure here. */
    public MyLinkedList() {
        head = new node(0);
        size = 0;

    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        if (index < 0 || index >= size) return -1;//特例
        node res = head;//
        for (int i = 0; i<index+1;i++){//这里得到的res的位置实际上是加上head的index-1的位置
            res = res.next;//对于同一个node，他的i=index-1
        }
        return res.val;

    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
        addAtIndex(0,val);

    }

    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        addAtIndex(size,val);

    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        if (index > size ) return;
        if (index < 0) index = 0;//特例
        node res = head;
        for (int i = 0; i<index;i++){//与get()类似，需要得到index-1的位置
            res = res.next;
        }//res为Index-1的node
        node insert = new node(val);
        insert.next = res.next;
        res.next = insert;
        size+=1;


    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if (index < 0||index>=size) return;
        node res = head;
        for (int i = 0; i<index;i++){
            res = res.next;
        }
        node d =  res.next.next;
        res.next = d;
        size-=1;

    }
}
//环形链表，两种办法
//哈希表（python中的dict），遍历查找是否有已经在哈希表里的节点
public boolean hasCycle(ListNode head) {
    Set<ListNode> nodesSeen = new HashSet<>();
    while (head != null) {
        if (nodesSeen.contains(head)) {
            return true;
        } else {
            nodesSeen.add(head);
        }
        head = head.next;
    }
    return false;
}
//双指针，用于检测环
//当慢指针移动一格，慢指针移动两格，如果有环，他们会相遇，来自弗洛伊德的龟兔赛跑

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {//特例
        return false;
    }
    ListNode slow = head;
    ListNode fast = head.next;
    while (slow != fast) {
        if (fast == null || fast.next == null) {//连续两个null证明没圈
            return false;
        }
        slow = slow.next;//龟走一步，兔走两步
        fast = fast.next.next;
    }
    return true;
        
    }
}

//反转链表
//递归
//特例为null或1-null，同时特例也可以检测递到最底层
//例如n-1-2-3-n, 先递到最底层3的地方，返回上层，此时head为2，p为3，将head.next.next = head
//即3指向2。再将2指向null，这样做是方便返回最顶层，也是防止当长度为2的链表产生环。
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}
//迭代
public ListNode reverseList(ListNode head) {
    ListNode prev = null;//上一个为null
    ListNode curr = head;//当前为head
    while (curr != null) {//停止条件当前为null
        ListNode nextTemp = curr.next;//储存下一个节点
        curr.next = prev;//当前节点指向上个节点
        prev = curr;//上个节点指针设置为当前节点
        curr = nextTemp;//当前节点指针设置为下个节点
    }
    return prev;
}
//迭代和递归的区别是，迭代是每次反转当前节点的指向，递归是反转下个节点的指向