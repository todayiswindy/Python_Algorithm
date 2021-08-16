t = int(input())

for _ in range(t):
    floor = int(input())
    room = int(input())

    f_list = [x for x in range(1, room + 1)]
    
    for i in range(floor):
        for j in range(1, room):
            f_list[j] += f_list[j - 1]
    
    print(f_list[-1])