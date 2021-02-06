import copy
import itertools

def check(dishes, conditions):
    count = 0
    for c in conditions:
        cond = copy.deepcopy(dishes)
        for e in c:
            cond.add(e)
        if dishes == cond:
            count += 1
    return count

def put_ball(balls):
    print(balls)
    dishes_patterns = []
    for b in balls:
        dishes_patterns = itertools.product(dishes_patterns, b)
    dishes = set()
    for d in dishes_patterns:
        if len(dishes) > len(set(d[0])):
            dishes = set(d)
        
    return(dishes)

if __name__ == '__main__':
    n, m = map(int, input().split())
    conditions = []
    for _ in range(m):
        a, b = map(int, input().split())
        conditions.append([a, b])

    k = int(input())
    balls = []
    for _ in range(k):
        c, d = map(int, input().split())
        balls.append([c, d])

    count = check(put_ball(balls), conditions)
    print(count)