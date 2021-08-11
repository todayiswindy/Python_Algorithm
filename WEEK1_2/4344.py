c = int(input())

for _ in range(c):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]

    count = 0
    for i in score[1:]:
        if i > avg:
            count += 1
    
    result = (count / score[0] * 100)
    print(f'{result:.3f}%')
    
    # print("%.3f" % (count / score[0] * 100) + "%")
