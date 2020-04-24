//今天不写码，回顾一下基础知识，以下都是java（结果还是写了）

//数据结构——队列queue
//FIFO
//以下是简单的队列实现，随着队伍的增大p_start指针会一直向前移动，浪费了空间
// "static void main" must be defined in a public class.

class MyQueue {
    // store elements
    private List<Integer> data;         
    // a pointer to indicate the start position
    private int p_start;            
    public MyQueue() {
        data = new ArrayList<Integer>();
        p_start = 0;
    }
    /** Insert an element into the queue. Return true if the operation is successful. */
    public boolean enQueue(int x) {
        data.add(x);
        return true;
    };    
    /** Delete an element from the queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (isEmpty() == true) {
            return false;
        }
        p_start++;
        return true;
    }
    /** Get the front item from the queue. */
    public int Front() {
        return data.get(p_start);
    }
    /** Checks whether the queue is empty or not. */
    public boolean isEmpty() {
        return p_start >= data.size();
    }     
};

public class Main {
    public static void main(String[] args) {
        MyQueue q = new MyQueue();
        q.enQueue(5);
        q.enQueue(3);
        if (q.isEmpty() == false) {
            System.out.println(q.Front());
        }
        q.deQueue();
        if (q.isEmpty() == false) {
            System.out.println(q.Front());
        }
        q.deQueue();
        if (q.isEmpty() == false) {
            System.out.println(q.Front());
        }
    }
}

//下面是循环队列的实现，在dequeue中注释了一些细节
class MyCircularQueue {
        private int[] data;
        private int p_start;
        private int p_end;
        private int size;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        data = new int[k];
        p_start = -1;
        p_end = -1;
        size = k;
        
        

    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (isFull() == true){
            return false;
        }
        if (isEmpty() == true){
            p_start = 0;
        }
        
        p_end = (p_end+1)%size;
        data[p_end] = value;
        return true;

    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {//dequeue不需要实际更新queue中的值，只需要移动头部指针即可
        if (isEmpty() == true){
            return false;
        }
        if (p_start == p_end){ //指向同一个值，也是最后一个值
            p_start = -1;
            p_end = -1;
            return true;
        }
        p_start = (p_start+1)%size;//循环的向前移动一位
        return true;
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        if  (isEmpty()==true){
            return -1;
        }
        return data[p_start];

    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        if  (isEmpty()==true){
            return -1;
        }
        return data[p_end];

    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return p_start == -1;

    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return ((p_end+1)%size) == p_start;

    }
}

//求队列中长度为k的移动窗口的平均值
class MovingAverage {
    private List<Integer> data;
    private int head;
    private int tail;
    private int gap;
    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        head = -1;
        tail = -1;
        gap = size;
        data = new ArrayList<Integer>();
    }
    
    public double next(int val) {
        double sum  = 0;
        if (head==-1){//当队列为初始状态时
            head+=1;
        }
        if (tail-head == gap-1){//前后指针之差小于gap-1
            head += 1;
        }
        tail += 1;
        data.add(val);
        //System.out.print(data.size());
        for (Integer value:data.subList(head,tail+1)){//遍历子队列
            sum += (double)value;
        }
        //System.out.print(sum/(tail-head+1));
        return (double)(sum/(tail-head+1));
        
        

    }
}

