n = int(input())
m = [500, 100, 50, 10, 5, 1]

a = 1000 - n
count = 0

for i in m:
    count += a // i
    a %= i
    
print(count)
