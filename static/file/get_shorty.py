import heapq


dist = []
visited = []


def dijkstra(graph, node):
    # initialize all arrays
    for _ in range(len(graph)):
        dist.append(float("-inf"))
        visited.append(False)
    dist[node] = 1

    # set up priority queue
    # invert weights to be max queue since we want largest size scale
    pq = []
    heapq.heappush(pq, (-1, node))

    while pq:
        # since no update on pq, we ignore entries for already visited items
        u = heapq.heappop(pq)[1]
        while visited[u] is True:
            if pq:
                u = heapq.heappop(pq)[1]
            else:
                break
        if visited[u] is False:
            visited[u] = True
        else:
            continue

        # main loop once valid u found
        for v in graph[u]:
            if dist[v] < dist[u] * graph[u][v]:
                dist[v] = dist[u] * graph[u][v]
                # we have to invert the weight for this to work
                heapq.heappush(pq, (-dist[v], v))


while True:
    # collect input
    maze = []
    dist = []
    visited = []
    mn = input().split(' ')

    # check if end
    if int(mn[0]) == 0 and int(mn[1]) == 0:
        exit()

    for _ in range(int(mn[0])):
        maze.append({})
    for _ in range(int(mn[1])):
        corridor = input().split(' ')
        maze[int(corridor[0])][int(corridor[1])] = float(corridor[2])
        maze[int(corridor[1])][int(corridor[0])] = float(corridor[2])

    # traverse
    dijkstra(maze, 0)

    # print result
    print("{0:0.4f}".format(dist[len(maze) - 1]))

