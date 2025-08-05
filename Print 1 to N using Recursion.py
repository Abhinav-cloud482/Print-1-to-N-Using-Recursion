N = int(input("Enter N: "))

stack = []
i = 1

while i <= N:
    stack.append(i)
    i += 1

while stack:
    print(stack.pop(0), end=' ')


