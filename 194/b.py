n = int(input())
a = list()
b = list()
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

total_list = list()
for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        if i == j:
            total_list.append(ai + bj)
        else:
            total_list.append(max(ai, bj))

print(min(total_list))