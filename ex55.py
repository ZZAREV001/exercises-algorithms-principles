# Fibonacci number calculation. Use iterative approach with 2 variables (O(n) time with
# n number of iterations and O(1) constant space).
def fib(n):
    a = 0            # assignment command: initialization of the 2 variables
    b = 1
    if n == 0:       # conditional command are used to manage a and b variables
        return a
    if n == 1:
        return b

    for _ in range(2, n + 1):    # iterative command with proper procedure calls command (include all values of n the Fibonacci suite)
        value = a + b

        a = b          # assignment command: update a with b with one iteration
        b = value      # assignment command: update b with value variable with one iteration
    return value       # return value variable (result of the Fibonacci's rule) when call fib(n) function


print(fib(9))
# expect result 34