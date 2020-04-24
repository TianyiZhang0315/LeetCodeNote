#1
#字典模拟哈希表
def twoSum(nums, target):
    print("nums",nums)
    hashmap={}
    for i,num in enumerate(nums):
        print("i=%d"%i)
        print("map before add",hashmap)
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target-num)]
        hashmap[num] = i
        print("map after add",hashmap)
        print("-"*20)
print(twoSum([3,2,3],6))
