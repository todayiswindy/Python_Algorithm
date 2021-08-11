n = int(input())

for _ in range(n):
    quiz = input()
    score = 0
    count = 0

    for i in range(len(quiz)):
        if quiz[i] == 'O':
            count += 1
            score += count
        else:
            count = 0
    
    print(score)
