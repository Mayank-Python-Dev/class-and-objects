def sort(nums):
    for i in range(6):
        minpos = i
        for j in range(i,7):
            if nums[j]<nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [7,9,1,3,4,5,8]
sort(nums)

print(nums)