n = int(input())
# an = [int(elm) for elm in input().split()]
an = map(float, input().split())

sum_an = 0
for a in an:
    sum_an += 1/a

print(1/sum_an)