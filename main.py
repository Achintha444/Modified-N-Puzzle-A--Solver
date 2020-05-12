from state import State #dim,state,goal,parent,moves
from constant import Constant

def findEvalFunMin(open):
    x = len(open)
    mi = open[0].evalFunCost
    st = open[0]
    j = 0
    for i in range(1,x):
        m = open[i].evalFunCost
        if (m<=mi):
            mi = m
            j = i
            st = open[i]
    return [st,j]
    
def aSearch(startState,goal):
    openList =[startState]
    closeList = []
    while(openList != []):
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
                if ((st not in openList) or (st not in closeList)):
                    openList.append(st)
                if ((st in openList) or (st in closeList)):
                    temp = st.evalFunCost
                    st.setGCost(min(st.gCost,(state.gCost+1)))
                    st.setEvalFunCost()
                    if ((st.evalFunCost<temp) and (st in closeList)):
                        openList.append(st)
    return None



print ("A* to solve the modified n-puzzle problem")
print ("-----------------------------------------")
print("")

n = int(input("Input the dimension of the n-puzzle : "))

state = []
goal = []
print("Input the start configuration (line by line)")
for i in range(n):
    state.append(list(map(str,str(input()).split("\t"))))
print("Input the goal configuration (line by line)")
for i in range(n):
    goal.append(list(map(str,str(input()).split("\t"))))

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