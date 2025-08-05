import math


class Student:
    def __init__(self, name):
        self.name = name
        self.friends = set()
        self.dist = math.inf


rumors = []
students = {}

# input
num_students = int(input())
for _ in range(num_students):
    new_student = input()
    students[new_student] = Student(new_student)

num_friendships = int(input())
for _ in range(num_friendships):
    friendship = input().split(' ')
    students[friendship[0]].friends.add(friendship[1])
    students[friendship[1]].friends.add(friendship[0])

num_rumors = int(input())
for _ in range(num_rumors):
    rumors.append(input())


for starter in rumors:
    # bfs for each rumor
    for s in students:
        if s == starter:
            students[s].dist = 0
        else:
            students[s].dist = math.inf

    queue = [starter]
    while queue:
        working = queue.pop(0)
        for friend in students[working].friends:
            if students[friend].dist == math.inf:
                queue.append(friend)
                students[friend].dist = students[working].dist + 1

    # print result
    max_depth = 0
    for student in students:
        if students[student].dist != math.inf and students[student].dist > max_depth:
            max_depth = students[student].dist

    i = 1
    print(starter, end="")
    while i <= max_depth:
        day = []
        for student in students:
            if students[student].dist == i:
                day.append(student)
        day = sorted(day)
        for student in day:
            print(" " + student, end="")
        i += 1
    last_day = []
    for student in students:
        if students[student].dist == math.inf:
            last_day.append(student)
    last_day = sorted(last_day)
    for student in last_day:
        print(" " + student, end="")
    print("", end="\n")

