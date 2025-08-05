import math


cities_sorted = []


class Node:
    def __init__(self, cost):
        self.cost = cost
        self.visited = False
        self.weight = math.inf
        self.children = {}


def explore(cities, city):
    city.visited = True
    for n in city.children.values():
        if n.visited is False:
            explore(cities, n)
    cities_sorted.append(city)


def dfs(cities):
    for city in cities.values():
        if city.visited is False:
            explore(cities, city)


def traverse(cities, src):
    stack = []
    for city in cities_sorted:
        stack.append(city)
    for city in cities.values():
        city.weight = math.inf
    src.weight = 0
    while len(stack) > 0:
        c = stack.pop()
        if c.weight != math.inf:
            for neighbor in c.children.values():
                if neighbor.weight > c.weight + neighbor.cost:
                    neighbor.weight = c.weight + neighbor.cost


# Gather input for nodes
cities = {}

num_cities = int(input())
for _ in range(num_cities):
    new_city = input().split(' ')
    cities[new_city[0]] = Node(int(new_city[1]))
num_roads = int(input())
for _ in range(num_roads):
    new_road = input().split(' ')
    cities[new_road[0]].children[new_road[1]] = cities[new_road[1]]


# dfs and topo sort
dfs(cities)

# handle traversals
num_traversals = int(input())
for _ in range(num_traversals):
    route = input().split(' ')
    src = cities[route[0]]
    dst = cities[route[1]]
    traverse(cities, src)

    if dst.weight == math.inf:
        print("NO")
    else:
        print(dst.weight)

