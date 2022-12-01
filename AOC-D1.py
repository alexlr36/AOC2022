filename = "input.txt"

with open(filename) as f:
    content = f.read().splitlines()
lst = []
currentTotal = 0
for line in content:
    if line == '':
        lst.append(currentTotal)
        currentTotal = 0
    else:
        currentTotal = currentTotal + int(line)
lst.sort(reverse=True)
total = 0
for topelf in range(3):
    total += lst[topelf]

print(total)