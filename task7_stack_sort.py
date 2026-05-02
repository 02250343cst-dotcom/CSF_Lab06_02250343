class Stack:
    def __init__(self):
        self.stack = []
 
    def push(self, item):
        self.stack.append(item)
 
    def pop(self):
        return self.stack.pop() if self.stack else None
 
    def display(self):
        return self.stack
 
    def to_list(self):
        return self.stack[:]
 
def selection_sort(lst):
    arr = lst[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
 
# Create and fill stack
s = Stack()
for item in [42, 15, 8, 73, 26]:
    s.push(item)
 
print(f"Stack contents: {s.display()}")
 
# Convert to list and sort
lst = s.to_list()
print(f"As list (before sort): {lst}")
sorted_lst = selection_sort(lst)
print(f"After selection sort:  {sorted_lst}")
 