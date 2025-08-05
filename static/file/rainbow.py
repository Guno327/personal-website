distance = []
cache = {}


def day(start, end):
    return int(pow(400 - (distance[end] - distance[start]), 2))


def penalty(i):
    if i in cache:
        return cache[i]
    elif i == count - 1:
        return 0
    else:
        cur_min = float("inf")
        for j in range(i+1, count):
            cur = day(i, j) + penalty(j)
            cur_min = min(cur_min, cur)
        cache[i] = cur_min
        return cur_min


count = int(input()) + 1
for _ in range(count):
    distance.append(int(input()))

print(penalty(0))
exit(0)
