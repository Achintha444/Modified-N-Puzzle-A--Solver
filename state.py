import math

from constant import Constant

class State:

    def __init__(self,dim,state,goal,parent,moves):
        self.dim = dim
        self.state = state
        self.goal = goal
        self.hCost = 0
        self.evalFunCost = 0
        self.heurisitic = ''
        self.moves = moves
        self.parent = parent
    
    def setHeuristic(self, heuristic):
        self.heuristic = heuristic
        if heuristic.lower().find(Constant.misplacedHeuristic) == 0:
            self.heuristicCost += self.getMisplacedHeuristic()
        elif heuristic.lower().find(Constant.ManhattanHeuristic) == 0:
            self.heuristicCost += self.getManhatanHeuristic()
    
    def getMisplacedHeuristic(self):
        misplacedHeuristicCost = 0
        for i in range (0,self.dim):
            for j in range(0,self.dim):
                temp = self.state[i][j]
                if temp != Constant.Blank:
                    if temp != self.goal[i][j]:
                        misplacedHeuristicCost+=1
        return misplacedHeuristicCost
    
    def getManhatanHeuristic(self):
        manhatanHeuristicCost = 0
        for i in range (0,self.dim):
            for j in range(0,self.dim):
                temp = self.state[i][j]
                if temp != Constant.Blank:
                    if temp != self.goal[i][j]:
                        correctPos = self.getCorrectCellFor(temp)
                        manhatanHeuristicCost+=abs(correctPos[0]-i-1)+abs(correctPos[1]-j-1)
        return manhatanHeuristicCost
    
    def getCorrectCellFor(self,number):
        num = int(number)
        for i in range (0,self.dim):
                if number in self.goal[i]:
                    # [row,col] of the correct postion
                    return [i+1,self.goal[i].index(number)+1]
    
    def isGoalState(self):
        return self.state==self.goal
    
    def getBlanksPos(self):
        # position will be [[row,col],[row,col]]
        pos = []
        count = 0
        for i in range(0,self.dim):
            if Constant.Blank in self.state[i]:
                pp = self.state[i].index(Constant.Blank)
                p = [i,pp]
                count +=1
                pos.append(p)
                for k in range(pp+1,self.dim):
                    if Constant.Blank == self.state[i][k]:
                        p = [i,k]
                        pos.append(p)
                        count+=1
            if count==2: break
        return pos
    
    def expand(self):
        expnad =[]
        blankPos= self.getBlanksPos()
        move = ["up","down","left","right"]
        for pos in blankPos:
            for m in move:
                shuffle = self.shuffle(m,pos)
                if shuffle is not None:
                    child = shuffle[0]
                    temp_moves = self.moves
                    child_moves = temp_moves.append([shuffle[1],m])
                    child_state = State(self.dim,child,self.goal,self,child_moves)
                    expnad.append(child_state)
                    #print expnad
        return expnad


    def shuffle(self,move,pos):
        new_pos = []
        if move == "right":
            new_pos = [pos[0],pos[1]-1]
        elif move=="left":
            new_pos = [pos[0],pos[1]+1]
        elif move=="down":
            new_pos = [pos[0]-1,pos[1]]
        elif move=="up":
            new_pos = [pos[0]+1,pos[1]]

        if new_pos[0] >= 0 and new_pos[0] < self.dim and new_pos[1] >= 0 and new_pos[1] < self.dim:
            # print self.state
            # print new_pos
            # print Constant.Blank
            if self.state[new_pos[0]][new_pos[1]]==Constant.Blank:
                return None
            else:
                a = self.copy()
                temp_state = a[:]
                print self.state
                temp = temp_state[new_pos[0]][new_pos[1]]
                temp_state[new_pos[0]][new_pos[1]] = "-"
                temp_state[pos[0]][pos[1]] = temp
                print self.state
                print ("sels state check")
                print temp_state
                print temp
                print move
                print "---------"
                return [temp_state,temp]
        else:
            return None

    def copy(self):
        temp = []
        for i in self.state:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

