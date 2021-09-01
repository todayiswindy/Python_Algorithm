listX = []
listY = []

for i in range(3):
    x, y = map(int, input().split())
    listX.append(x)
    listY.append(y)

for i in range(3):
    if listX.count(listX[i]) == 1:
        x = listX[i]
    if listY.count(listY[i]) == 1:
        y = listY[i]

print(x, y)