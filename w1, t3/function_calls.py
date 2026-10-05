def double(n):
    print("\nA")
    n = n * 2
    return n

x = 5
y = double(x)
print(x, y)

def shout(word):
    print("\nB")
    print(word.upper())

result = shout("hi")
print(result)

def add_one(num):
    print("\nC")
    num.append(1)

a = [7]
b = a
add_one(a)
print(a, b)

print("\nD")
def first_even(nums):
    for num in nums:
        if num % 2 == 0:
            return num

    return None

print(first_even([3, 8, 5, 4]))
print(first_even([3, 5]))

print("\nE")
a = [1, 2]
b = a
b = [9]
print(a, b)

print("\nF")
def get_total(nums):
    total = 0
    for num in nums:
        total += num
    return total

x = get_total([1,2])
print(x + 1)

print("\nG")
def remove_last(items):
    items.pop()
    return len(items)

todo = ["a", "b", "c"]
done = todo
n = remove_last(todo)
print(n, todo, done)