info_line = input().split(' ')
n = int(info_line[0])
j = int(info_line[1])
values = [[0 for x in range(2)] for y in range(n)]
cache = {}


def max_value(r, limit, k):
    if (r, limit, k) in cache:
        return cache[(r, limit, k)]

    result = 0
    if r == n:
        return 0
    elif k == n - r:
        if limit == 0:
            result = values[r][0] + max_value(r+1, 0, k-1)
        elif limit == 1:
            result = values[r][1] + max_value(r+1, 1, k-1)
        elif limit == -1:
            result = max(values[r][0] + max_value(r+1, 0, k-1),
                         values[r][1] + max_value(r+1, 1, k-1))
    elif k < n - r:
        if limit == 0:
            result = max(values[r][0] + max_value(r+1, 0, k-1),
                         values[r][0]+values[r][1] + max_value(r+1, -1, k))
        elif limit == 1:
            result = max(values[r][1] + max_value(r+1, 1, k-1),
                         values[r][0]+values[r][1] + max_value(r+1, -1, k))
        elif limit == -1:
            result = max(values[r][0] + max_value(r+1, 0, k-1),
                         values[r][1] + max_value(r+1, 1, k-1),
                         values[r][0] + values[r][1] + max_value(r+1, -1, k))

    cache[(r, limit, k)] = result
    return result


for i in range(n):
    line = input().split(' ')
    values[i][0] = int(line[0])
    values[i][1] = int(line[1])

print(max_value(0, -1, j))
