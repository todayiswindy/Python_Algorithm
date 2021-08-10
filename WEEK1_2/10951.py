import sys

for n in sys.stdin:
    a, b = map(int, n.split())
    print(a + b)