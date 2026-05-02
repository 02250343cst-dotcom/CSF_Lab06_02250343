def selection_sort_trace(lst):
    arr = lst[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Pass {i + 1}: {arr}")
    return arr
 
numbers = [64, 25, 12, 22, 11]
print(f"Original List: {numbers}")
print("--- Sorting Trace ---")
result = selection_sort_trace(numbers)
print(f"Final Sorted List: {result}")