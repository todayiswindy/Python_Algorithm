n = int(input())
count = 0

for num in range(1, n + 1):
    if num < 100:
        count += 1
    else:
        arr = list(map(int, str(num)))
        if arr[1] - arr[0] == arr[2] - arr[1]:
            count += 1

print(count)