

dictionary = []
solutions = []
rejected = []

nk = input().split(' ')
for i in range(0, int(nk[0])):
    dictionary.append(input())

for w in dictionary:
    swl = sorted(w)
    sw = ''
    for c in swl:
        sw += c
    if sw in solutions:
        solutions.remove(sw)
        rejected.append(sw)
    elif sw not in rejected:
        solutions.append(sw)
print(len(solutions))
