import math


def climb(count, move_list):

    # max possible height
    s = sum(move_list)

    # max can't be odd
    if s % 2 == 1:
        print("IMPOSSIBLE")
        return

    height = [[math.inf for x in range(s + 1)] for x in range(count)]
    path = [['' for x in range(s + 1)] for x in range(count)]

    # first move always goes up
    height[0][move_list[0]] = move_list[0]
    path[0][move_list[0]] = 'U'

    # test all options, choose best
    for i in range(1, count):
        for j in range(s + 1):
            if height[i - 1][j] != math.inf:
                if j >= move_list[i]:
                    if height[i][j - move_list[i]] > height[i - 1][j]:
                        path[i][j - move_list[i]] = 'D'
                        height[i][j - move_list[i]] = height[i - 1][j]
                temp_opt = max(height[i - 1][j], j + move_list[i])
                if height[i][j + move_list[i]] > temp_opt:
                    path[i][j + move_list[i]] = 'U'
                    height[i][j + move_list[i]] = temp_opt

    # did not reach street level
    if height[count - 1][0] == math.inf:
        print("IMPOSSIBLE")
        return

    # construct result
    result = ["" for x in range(count)]
    j = 0
    for k in reversed(range(count)):
        if path[k][j] == 'U':
            j -= move_list[k]
            result[k] = "U"
        else:
            j += move_list[k]
            result[k] = "D"
    print("".join(result))


num_tests = int(input())
for _ in range(num_tests):

    num_moves = int(input())
    moves = [int(numeric_string) for numeric_string in input().split(' ')]
    climb(num_moves, moves)
