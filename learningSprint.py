

def sort(nums, target):
    pivot = 0
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            pivot = i
    if target in nums:
        return nums.index(target) - pivot
    else:
        return -1
print(sort([4,5,6,7,0,1,2], 1))