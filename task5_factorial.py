def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
 
n = int(input("Enter number: "))
print(f"Iterative factorial = {factorial_iterative(n)}")
print(f"Recursive factorial = {factorial_recursive(n)}")
 