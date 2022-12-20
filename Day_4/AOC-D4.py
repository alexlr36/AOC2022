#filename = "./Day_4/test_input.txt"
filename = "./Day_4/input.txt"

with open(filename) as f:
    content = f.read().splitlines()

totalPairs = 0

def doesItContain(list1, list2):
    #result = True
    for i in list1:
        if i not in list2:
            return False
    #print(list1, " contains: ", list2, "\n")
    return True

for s in content:
    elves = s.split(',')
    elve1 = elves[0].split('-')
    elve2 = elves[1].split('-')
    
    #print("elve1 is: ", elve1, "\n", "and elve2 is: ", elve2)
    
    elve1List = []
    elve2List = []
    # add values
    for intr in range(int(elve1[0]), (int(elve1[1]) + 1)):
        elve1List.append(intr)
    for intr in range(int(elve2[0]), (int(elve2[1]) + 1)):
        elve2List.append(intr)
    if doesItContain(elve1List, elve2List) or doesItContain(elve2List, elve1List):
        totalPairs = totalPairs + 1

print("Total assignment pairs: ", totalPairs, "\n")

## PART 2
overlappingPairs = 0

def doesItContain(list1, list2):
    #result = True
    for i in list1:
        if i in list2:
            return True
    #print(list1, " contains: ", list2, "\n")
    return False

for s in content:
    elves = s.split(',')
    elve1 = elves[0].split('-')
    elve2 = elves[1].split('-')
    
    #print("elve1 is: ", elve1, "\n", "and elve2 is: ", elve2)
    
    elve1List = []
    elve2List = []
    # add values
    for intr in range(int(elve1[0]), (int(elve1[1]) + 1)):
        elve1List.append(intr)
    for intr in range(int(elve2[0]), (int(elve2[1]) + 1)):
        elve2List.append(intr)
    if doesItContain(elve1List, elve2List) or doesItContain(elve2List, elve1List):
        overlappingPairs = overlappingPairs + 1
        
print("Overlapping assignment pairs: ", overlappingPairs, "\n")
