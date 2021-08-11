n = int(input())
num = list(map(int, input().split()))

biggest = num[0]
smallest = num[0]

for i in num:
    if i > biggest:
        biggest = i
    if i < smallest:
        smallest = i
    
print("%d %d" % (smallest, biggest))

# n = int(input())
# num = list(map(int, input().split()))
# print("{} {}".format(min(num), max(num)))