def max_num(num):
    return sorted(list(num), reverse=True)[0]

def n_ary(x: str, d: int):
    size = len(x)
    total = 0
    for s in range(size):
        e = int(x[s]) * (d ** (size - s - 1))
        total += e
    return total

if __name__ == '__main__':
    x = input()
    m = input()
    d = int(max_num(x))
    count = 0
    while True:
        d += 1
        converted = n_ary(x, d)
        if int(m) < converted:
            break
        else:
            count += 1
    print(count)
    