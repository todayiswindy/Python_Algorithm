n = int(input())
score = list(map(int, input().split()))
M = max(score)
newScore = []

for num in score: 
    newScore.append(num / M * 100)

aveScore = sum(newScore) / n
print(aveScore)