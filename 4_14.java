//今天复习二分查找

class Solution {
    public int search(int[] nums, int target) {
    int pivot, left = 0, right = nums.length - 1;//定义左右和pivot中间指针
    while (left <= right) {//当左小于等于右时循环
      pivot = left + (right - left) / 2;//中间等于左指针加上左右距离的一半
      if (nums[pivot] == target) return pivot;//如果此时pivot为目标，则返回
      if (target < nums[pivot]) right = pivot - 1;//若目标比中间小，取左区间，左指针不动，右指针放置在pivot-1
      else left = pivot + 1;
    }
    return -1;
  }


}//初始条件：left = 0, right = length-1
//终止：left > right
//向左查找：right = mid-1
//向右查找：left = mid+1

//正确的流程分为三步
//1.预处理：如果集合未排序，则先排序
//2.二分查找：使用循环或者递归每次比较后将查找空间分为两半
//3.后处理：在剩余查找空间中确定候选者

//第一个错误的版本
//1到n，在k之前都是false,k开始都是true,找到k
//当mid为false，更新left = mid+1，反之，更新right = mid
//因为java的整除是round down的，所以左边界每次更新到mid+1

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        if (isBadVersion(1)){
            return 1;
        }
        while (left < right){
            int mid = left + (right - left)/2;
            if (isBadVersion(mid)){
                if (!isBadVersion(mid-1)){
                    return mid;
                }
                right = mid;
            }else{
                if (isBadVersion(mid+1)){
                    return mid+1;
                }
                left = mid+1;
            }
        
        }
        return -1;
        
    }
}

//在排序数组中查找元素的第一个和最后一个位置
//首先用普通的二分查找第一次找到目标值，以目标值左区域二分查找左边界，若mid>0且mid-1位置的值也是目标值
//则将右指针放置到mid-1位置,若mid-1的值与mid不同或mid=0，则返回mid
class Solution {
    public int[] searchRange(int[] nums, int target) {
        if(nums==null) {
            return new int[]{-1,-1};
        }
        int firstIndex = find(true,nums,target);
        int lastIndex = find(false,nums,target);
        return new int[]{firstIndex,lastIndex};
    }

    //查找第一个和最后一个元素
    private int find(boolean isFindFirst,int[] nums,int target) {
        int begin = 0;
        int end = nums.length-1;
        //if和else if的逻辑跟正常的二分查找一样
        while(begin<=end) {
            int mid = begin+(end-begin)/2;
            if(nums[mid]>target) {
                end = mid-1;
            }
            else if(nums[mid]<target) {
                begin = mid+1;
            }
            //找到目标值了，开始定位到第一个和最后一个位置
            else {
                //查找第一个和最后一个逻辑很类似，这里用一个变量标记
                //是查找第一个还是查找最后一个
                if(isFindFirst) {
                    //如果不满足条件，缩小右边界，继续往左边查找
                    if(mid>0 && nums[mid]==nums[mid-1]) {//例如进入时mid为0，直接返回
                    	                                 //例如进入时mid为1，左侧非目标值直接返回
                    									 //左侧为目标值则mid=0，下个循环返回mid=0
                        end = mid-1;
                    } else {
                        return mid;
                    }
                }
                else {
                    //如果不满足条件，增大左边界，继续往右边查找
                    if(mid<nums.length-1 && nums[mid]==nums[mid+1]) {
                        begin = mid+1;
                    } else {
                        return mid;
                    }
                }
            }
        }
        return -1;
    }
}