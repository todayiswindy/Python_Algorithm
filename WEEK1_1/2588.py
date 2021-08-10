a, b = map(int, input().split())
print(a * (b % 10))
print(a * int((b % 100) / 10))
print(a * int(b / 100))
print(a * b)

# a = int(input())
# b = input()
# print(a * int(b[2]), a * int(b[1]), a * int(b[0]), a * int(b), sep='\n')