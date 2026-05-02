class Queue:
    def __init__(self):
        self.queue = []
 
    def enqueue(self, item):
        self.queue.append(item)
 
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
 
    def display(self):
        return self.queue
 
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i + 1  # 1-based position
    return -1
 
# Create and fill queue
q = Queue()
for item in [11, 33, 55, 77, 99]:
    q.enqueue(item)
 
print(f"Queue contents: {q.display()}")
target = int(input("Enter element to search: "))
result = linear_search(q.display(), target)
if result != -1:
    print(f"Element found at position {result} in the queue")
else:
    print("Element not found in the queue")
