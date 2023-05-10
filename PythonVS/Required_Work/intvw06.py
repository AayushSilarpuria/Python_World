def find_unique(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num

nums = [4, 1, 2, 1, 2]
unique_num = find_unique(nums)
print(unique_num)