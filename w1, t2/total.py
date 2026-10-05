# will need a total/sum variable to keep track of sum
# loop over the list of numbers
# add each item to the total
# return the total
def total(nums):
    result = 0
    for num in nums:
        result += num

    return result

print(total([2, -4, -5, 9, 2, 3]))