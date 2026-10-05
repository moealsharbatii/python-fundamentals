# make a count variable to keep track of how many evens we run into
# loop over the list of numbers
# if a number mod 2 equals 0, then add to the count, otherwise don't add
# return the count
def count_evens(nums):
    count = 0
    for num in nums:
        if(num % 2 == 0):
            count += 1

    return count

print(count_evens([2, -4, -5, 9, 2, 3]))