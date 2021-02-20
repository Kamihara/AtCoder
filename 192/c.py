
def g1(num):
    ordered_num = int(''.join(sorted(list(str(num)), reverse=True)))
    return ordered_num

def g2(num):
    ordered_num = int(''.join(sorted(list(str(num)), reverse=False)))
    return ordered_num

if __name__ == '__main__':
    n, k = map(int, input().split())
    for _ in range(k):
        f = g1(n) - g2(n)
        n = f

    print(n)