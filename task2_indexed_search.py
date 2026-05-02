import math
 
def indexed_search(lst, target):
    n = len(lst)
    block_size = int(math.sqrt(n))
 
    # Find the block where the element might be
    prev = 0
    while prev < n and lst[min(prev + block_size, n) - 1] < target:
        prev += block_size
        if prev >= n:
            return False

    # Linear search within the identified block
    for i in range(prev, min(prev + block_size, n)):
        if lst[i] == target:
            return True
    return False

numbers = [5, 10, 15, 20, 25, 30]
print(f"List: {numbers}")
target = int(input("Enter element: "))
if indexed_search(numbers, target):
    print("Element found")
else:
    print("Element not found")
 