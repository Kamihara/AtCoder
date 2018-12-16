n, m = map(int, input().split())
l = []

for i in range(m):
    y, p = map(int, input().split())
    l.append([y, p])

l.sort()
print(l)

