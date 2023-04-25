# Reverse Polish notation calculator
def calculate(inputs):
    stack = []

    for i in inputs:
        if i in ('-', '+', '*', '/'):
            b = stack.pop()
            a = stack.pop()
            if i == '-':
                stack.append(a - b)
            if i == '+':
                stack.append(a + b)
            if i == '*':
                stack.append(a * b)
            if i == '/':
                stack.append(a / b)
        else:
            stack.append(i)
    return stack[0]


print(calculate([1, 2, 3, '+', 2, '*', '-']))
# expect 9 as result of calculator operation: 1 - (2 + 3) * 2 = -9