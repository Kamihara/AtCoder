a, b = map(int, input().split())
nyu_kokei = a + b

if nyu_kokei >= 15 and b >= 8:
    print(1)
elif nyu_kokei >= 10 and b >= 3:
    print(2)
elif nyu_kokei >= 3:
    print(3)
else:
    print(4)