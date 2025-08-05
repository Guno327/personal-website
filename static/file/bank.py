people = {}

total_sum = 0

info = input().split(' ')
num_people = int(info[0])
num_minutes = int(info[1])

for _ in range(num_people):
    person = input().split(' ')
    people.setdefault(int(person[1]), []).append(int(person[0]))

candidates = []
for i in range(num_minutes)[::-1]:
    if i in people.keys():
        for money in people[i]:
            candidates.append(money)
        if candidates:
            total_sum += max(candidates)
            candidates.remove(max(candidates))

print(total_sum)
