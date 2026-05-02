call_count = 0
 
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
 
def fibonacci_recursive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
 
n = 10
print(f"Fibonacci({n}) - Iterative: {fibonacci_iterative(n)}")
 
call_count = 0
result = fibonacci_recursive(n)
print(f"Fibonacci({n}) - Recursive: {result}")
print(f"Recursive calls made: {call_count}")
 
print("\n--- Efficiency Comparison ---")
print(f"Iterative: O(n) time, O(1) space")
print(f"Recursive: O(2^n) time, O(n) stack space")
print(f"For n={n}, recursive made {call_count} calls vs iterative's {n-1} iterations")