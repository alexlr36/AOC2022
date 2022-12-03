filename = "./input.txt"

with open(filename) as f:
    content = f.read().splitlines()

lst = []
currentTotal = 0
strat_total = 0

for line in content:
    curr = line.split()
    # calc score
    # rock A beats Z, Ties on X and loses and Y
    if curr[0] == 'A':
        # Rock beats sizors
        if curr[1] == 'X':
            currentTotal = currentTotal + 3 + 1
            strat_total = strat_total + 3
        # Rock ties rock
        elif curr[1] == 'Y':
            currentTotal = currentTotal + 6 + 2
            strat_total = strat_total + 3 + 1 
        # Rock loses to paper
        elif curr[1] == 'Z':
            currentTotal = currentTotal + 0 + 3
            strat_total = strat_total + 6 + 2
    elif curr[0] == 'B':
        # Paper beats rock
        if curr[1] == 'X':
            currentTotal = currentTotal + 0 + 1
            strat_total = strat_total + 1
        # Paper ties with paper
        elif curr[1] == 'Y':
            currentTotal = currentTotal + 3 + 2
            strat_total = strat_total + 3 + 2
        # Paper loses to sizors
        elif curr[1] == 'Z':
            currentTotal = currentTotal + 6 + 3
            strat_total = strat_total + 6 + 3
    elif curr[0] == 'C':
        # Sizors beats paper
        if curr[1] == 'X':
            currentTotal = currentTotal + 6 + 1
            strat_total = strat_total + 2
        # Sizors ties on sizors
        elif curr[1] == 'Y':
            currentTotal = currentTotal + 0 + 2
            strat_total = strat_total + 3 + 3
        # Sizors loses to rock
        elif curr[1] == 'Z':
            currentTotal = currentTotal + 3 + 3
            strat_total = strat_total + 6 + 1

print(currentTotal)
print(strat_total) 