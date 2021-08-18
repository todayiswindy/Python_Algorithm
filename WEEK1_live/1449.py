n, l = map(int, input().split())
pos = list(map(int, input().split()))

pos.sort()

cnt = 1
start = pos[0]
end = pos[0] + l

for i in range(n):
    if start <= pos[i] < end:
        continue
    else:
        start = pos[i]
        end = pos[i] + l
        cnt += 1

print(cnt)