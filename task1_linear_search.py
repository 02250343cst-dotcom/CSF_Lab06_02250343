def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i + 1  # 1-based position
    return -1
 
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
target = int(input("Enter element to search: "))
result = linear_search(numbers, target)
if result != -1:
    print(f"Element found at position {result}")
else:
    print("Element not found")
 