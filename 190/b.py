def eisho(jumon, s, d):
    for j in jumon:
        eisho = j[0]
        damage = j[1]
        if s > eisho and d < damage:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    n, s, d = map(int, input().split())
    jumon = []
    for _ in range(n):
        x, y = map(int, input().split())
        jumon.append([x, y])
    print(eisho(jumon, s, d))