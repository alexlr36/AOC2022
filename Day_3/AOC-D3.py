# filename = "./Day_3/test1.txt"
filename = "./input.txt"

def assignPrior(l, n):
    return {l : n}

list_upper = list(map(chr, range(65, 91)))
list_lower = list(map(chr, range(97, 123)))
prior = {}
for i in range(0, 26):
    prior.update(assignPrior(list_lower[i], i + 1))
for i in range(27, 53):
    prior.update(assignPrior(list_upper[(i - 27)], i))


sum = 0;
with open(filename) as f:
    content = f.read().splitlines()
    charlst1 = {}
    charlst2 = {}
    charlst3 = {}
    charlstlst = {0: charlst1, 1:charlst2, 2:charlst3}
    currElf = 0
    current_val = 1
    for s in content:
        # half = len(s) / 2
        # frstLst = s[:int(half)]
        # secndhalf = s[int(half):]
        for i in range(0, len(s)):
            currcharlist = charlstlst.get(currElf)
            currcharlist.update({s[i]: i})

        if (current_val % 3) == 0:
            for c in charlst1:
                if (charlst2.get(c) != None) and (charlst3.get(c) != None):
                    print("printing badge of the current 3 elves: " + c + ": " + str(prior[c]))
                    sum += prior[c]
                    print("sum is: " + str(sum))
            print()
            print()
            current_val = 1
            currElf = 0
            charlst1.clear()
            charlst2.clear()
            charlst3.clear()
        else:
            current_val = current_val + 1
            currElf = currElf + 1
        
 
print(sum)