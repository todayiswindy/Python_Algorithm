t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    cnt = 0
    move = 1
    sum = 0

    while sum < d:
        cnt += 1
        sum += move
        
        if cnt % 2 == 0:
            move += 1
    
    print(cnt)