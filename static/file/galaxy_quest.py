import math


class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_distance(star1, star2, d):
    if math.pow((star1.x - star2.x), 2) + math.pow((star1.y - star2.y), 2) < math.pow(d, 2):
        return True
    return False


def galaxy_count(array, element, d):
    count = 0
    for a in array:
        if check_distance(a, element, d):
            count += 1
    return count


def check_galaxies(star_list, d):
    # base cases
    if len(star_list) == 0:
        return None
    elif len(star_list) == 1:
        return star_list[0]
    # work
    y = None
    star_list_prime = []
    for s in range(0, len(star_list), 2):
        if s+1 == len(star_list):
            y = star_list[s]
            break
        if check_distance(star_list[s], star_list[s+1],d):
            star_list_prime.append(star_list[s])
    x = check_galaxies(star_list_prime, d)
    if x is None:
        if len(star_list) % 2 == 1:
            if galaxy_count(star_list, y, d) > len(star_list) / 2:
                return y
    elif galaxy_count(star_list, x, d) > len(star_list) / 2:
        return x
    return None


# Collect input
dk = input().split(' ')
d = int(dk[0])
k = int(dk[1])

stars = []
for i in range(0, k):
    line = input().split(" ")
    obj = Star(int(line[0]), int(line[1]))
    stars.append(obj)

# Calculate
candidate = check_galaxies(stars, d)
if candidate is not None:
    print(galaxy_count(stars, candidate, d))
else:
    print("NO")

