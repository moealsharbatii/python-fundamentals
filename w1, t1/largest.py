def find_largest(nums):
    if nums == []:
        return None
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num

    return largest

print(find_largest([3, 5, 9]))
print(find_largest([-4, -2, -7]))
print(find_largest([9, 5, 3]))
print(find_largest([]))