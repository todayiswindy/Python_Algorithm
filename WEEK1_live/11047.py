n, k = map(int, input().split())
v = []
cnt = 0

for _ in range(n):
    v.append(int(input()))

v.sort(reverse = True)

for i in v:
    if k == 0:
        break
    cnt += k // i
    k %= i

print(cnt)