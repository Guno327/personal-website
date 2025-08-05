import math

min_weight = math.inf
visited = {}
best = math.inf


def tsp(cur_v, cur_weight, cur_depth, depth, graph):
    # I was having issues with scope, this is to make sure I am using the above defined vars (yay python!)
    global min_weight, visited, best

    # If this choice + remaining lower bound is worse than best no need to continue
    if (cur_weight + (depth - cur_depth) * min_weight) >= best:
        return
`
    # final step is to return back to start
    if cur_depth == depth - 1:
        best = min(best, cur_weight + graph[cur_v][0])

    # Main loop, test all possible paths in order
    else:
        for v in range(depth):
            if v not in visited:
                visited[v] = True
                tsp(v, cur_weight + graph[cur_v][v], cur_depth + 1, depth, graph)
                del visited[v]


n = int(input())
g = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    current = input().split(' ')
    for j in range(n):
        g[i][j] = int(current[j])
        min_weight = min(min_weight, int(current[j]))

visited[0] = True
tsp(0, 0, 0, n, g)
print(best)
