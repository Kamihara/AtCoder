n = int(input())
vn = list(map(int, input().split()))

def merge(x, y):
    return (x + y) / 2

for _ in range(n-1):
    vn = sorted(vn)
    x = vn.pop(0)
    y = vn.pop(0)
    vn.append(merge(x, y))

print(vn[0])