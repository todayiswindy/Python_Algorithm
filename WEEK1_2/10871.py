n, x = map(int, input().split())
num = list(map(int, input().split()))
for i in range(x):
    if num[i] < x:
        print(num[i], end = " ")