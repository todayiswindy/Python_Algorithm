t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    room = n // h + 1
    floor = n % h
    
    if n % h == 0:
        room = n // h
        floor = h
    
    print(f'{floor * 100 + room}')