n = []

for _ in range(10):
    a = int(input())
    b = a % 42
    n.append(b)

result = set(n)
print(len(result))