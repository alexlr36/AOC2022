# filename = "./Day_5/test_input.txt"
filename = "./Day_5/input.txt"

# testStack = [['Z','N'],
#              ['M','C','D'],
#              ['P']]

MainStacks = [
    ['Q','F','M','R','L','W','C','V'],
    ['D','Q','L'],
    ['P','S','R','G','W','C','N','B'],
    ['L','C','D','H','B','Q','G'],
    ['V','G','L','F','Z','S'],
    ['D','G','N','P'],
    ['D','Z','P','V','F','C','W'],
    ['C','P','D','M','S'],
    ['Z','N','W','T','V','M','P','C']]

stacks = MainStacks

#print("test stack: ", testStack, "\n")

with open(filename) as f:
    content = f.read().splitlines()

def doPart1():    
    for s in content:
        if s.__contains__("move"):
            # command1[0] = 'move 1 '
            # command1[1] = ' 9 to 2'
            command1 = s.split("from")
            frm = command1[1].split('to')
            frm0 = int(frm[0].split(' ')[1]) - 1
            to = int(frm[1].split(' ')[1]) - 1
            move = int((command1[0].split(' '))[1].split(' ')[0])
            print("move", move, "from ", frm0,"->", to,"\n")
            
            for i in range(0, int(move)):
                tmp = (stacks[int(frm0)])
                tmpval = tmp[(len(tmp) - 1)]
                del (stacks[int(frm0)])[len(tmp) - 1]
                stacks[int(to)].append(tmpval)
            print("result is: ", stacks, "\n")

    for crt in stacks:
        print(crt[len(crt) - 1], "\n")

#---------PART 2 --------------

print("\n part 2 \n")

stackedVals = []

def doPart2():
    for s in content:
        if s.__contains__("move"):
            # command1[0] = 'move 1 '
            # command1[1] = ' 9 to 2'
            command1 = s.split("from")
            frm = command1[1].split('to')
            frm0 = int(frm[0].split(' ')[1]) - 1
            to = int(frm[1].split(' ')[1]) - 1
            move = int((command1[0].split(' '))[1].split(' ')[0])
            print("move", move, "from ", frm0,"->", to,"\n")
            
            stackedVals= []     
            for i in range(0, int(move)):
                tmp = (stacks[int(frm0)])
                tmpval = tmp[(len(tmp) - 1)]
                del (stacks[int(frm0)])[(len(tmp) - 1)]
                stackedVals.append(tmpval)
            if (len(stackedVals) - 1) > 0:
                stklen = (len(stackedVals) - 1)  
                j = stklen
                for i in range(0, len(stackedVals)):
                    stacks[int(to)].append(stackedVals[j - i])
            else:
                stacks[int(to)].append(stackedVals[0])
            print("result is: ", stacks, "\n")

    for crt in stacks:
        print(crt[len(crt) - 1], "")
        
doPart2()