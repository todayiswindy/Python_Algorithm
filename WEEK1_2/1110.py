n = int(input())
num = n
count = 0

while True:
    a = int(num / 10)
    b = num % 10

    new = (a + b) % 10 + b % 10 * 10
    count += 1
    
    if new == n:
        break
    num = new

print(count)