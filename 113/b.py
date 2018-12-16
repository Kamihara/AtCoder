n = int(input())
t, a = map(int, input().split())
h = [int(elm) for elm in input().split()]
l = []

for x in h:
    l.append(abs(a - (t - x * 0.006)))

print(l.index(min(l)) + 1)