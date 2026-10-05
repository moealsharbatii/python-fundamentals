# loop over the list of number
# will need a 'smallest' variable, and can equate to the first 'num' (item) in the list
# keep looping and compare with the rest of the list, and seeing if we run into another smallest value
def find_smallest(nums):
    smallest = nums[0]
    for num in nums:
        if(num < smallest):
            smallest = num

    return smallest


print(find_smallest([2, -4, -5, 9, 2, 3]))