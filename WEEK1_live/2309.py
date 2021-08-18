h = []

for _ in range(9):
    h.append(int(input()))
h.sort()
sum = sum(h)

for i in range(9):
    for j in range(i + 1, 9):
        if sum - (h[i] + h[j]) == 100:
            m, n = h[i], h[j]

h.remove(m)
h.remove(n)

for i in range(len(h)):
    print(h[i])