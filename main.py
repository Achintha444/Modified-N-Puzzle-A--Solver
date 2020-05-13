from state import State #dim,state,goal,parent,moves
from constant import Constant

def is_in_CLOSED(state,closeList):
    for closed_state in closeList:
        if closed_state.state == state.state:
            return True
    return False

def is_in_OPEN(state,openList):
    for open_state in openList:
        if open_state.state == state.state:
            return True
    return False

def get_open_state(state,openList):
    for open_state in openList:
        if open_state.state == state.state:
            return open_state


def findEvalFunMin(open):
    x = len(open)
    mi = open[0].evalFunCost
    st = open[0]
    j = 0
    for i in range(1,x):
        m = open[i].evalFunCost
        if (m<mi):
            mi = m
            j = i
            st = open[i]
    return [st,j]
    
def aSearch(startState,goal):
    openList =[startState]
    closeList = []
    while(openList != []):
        #print (len(openList))
        xx = findEvalFunMin(openList)
        state = xx[0]
        openList.pop(xx[1])
        closeList.append(state)

        if state.isGoalState():
            print (state.moves)
            print (state.state)
            return state
        else:
            ex = state.expand()
            for st in ex:
                if is_in_CLOSED(st,closeList):
                    continue
                if not(is_in_OPEN(st,openList)):
                    openList.append(st)
                else:
                    open_state = get_open_state(st,openList)
                    if st.gCost < open_state.gCost:
                        open_state.gCost = st.gCost
                        open_state.setEvalFunCost()
                        open_state.parent = st.parent
    return None

print ("A* to solve the modified n-puzzle problem")
print ("-----------------------------------------")
print("")

n = int(input("Input the dimension of the n-puzzle : "))

state = []
goal = []


files = list(list(map(str,str(input("Input the input configuration file and the goal configuration file (as tabbed inputs) : ")).split("\t"))))

fo = open(files[0], "r")
lines = fo.readlines()

for line in lines:
    state.append(line.strip().split())
fo.close()

fo = open(files[1], "r")
lines = fo.readlines()
for line in lines:
    goal.append(line.strip().split())
fo.close()

print ("Enter the number infront to select the heuristic :")
print ("1 - number of misplaced tiles")
print ("2 - total Manhattan distance")
x = int(input("Enter the value : "))


startState= State(n,state,goal,None,[])
if (x==1):
  startState.setHeuristic(Constant.MisplacedHeuristic)
elif (x==2):
  startState.setHeuristic(Constant.ManhattanHeuristic)
startState.setGCost(0)
startState.setEvalFunCost()

g = aSearch(startState,goal)

output = ""
for item in g.moves:
  a= "("+item[0]+","+item[1]+")"+", "
  output+=a
output=output[:-2]

fo = open('output.txt',"w+")
fo.write(output)
fo.close()

print('')
print ('-- necessary moves will be saved to output.txt --')
print('')
ex = str(input('Press any key to exit : '))
exit()