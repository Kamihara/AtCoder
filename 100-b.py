d, n  = map(int, input().split())

if d == 0:
    if n == 100:
        print(101)
    else:
        print(1 * n)
if d == 1:
    if n == 100:
        print(10100)
    else:
        print(100 * n)
if d == 2:
    if n == 100:
        print(1010000)
    else:
        print(10000 * n)
