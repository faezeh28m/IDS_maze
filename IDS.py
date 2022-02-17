#Tamrin 1
#IDS
#Faezeh Movahedi
             
#Open Maze:
from typing import Counter


file = open ("Maze.txt" , "r")
maze = file.read().split()

# for i in maze:
#     print (i)


class Node:  
    def __init__(self , s , p , d):
        self.state= s
        self.parent = p
        self.depth = d
        #state = (x,y)
        #parent = Pointing to the parent node
        

goal_state = maze[15][30]
# print (goal_node)

def IDS():
    
    #start_point = maze[15][0] => state = (15,0)
    start_node = Node ([15,0] , None , 0)
    
    import sys
    for L in range(0,sys.maxsize**10):
        print ("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ next L @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        frontier = [start_node]
        explored = []
        print ('L = ' , L)
        # if start_node.state == [15,30]:
        #     print ('goal is find')
        #     return start_node
        counter = 0 

        if start_node.depth == L:
            print ("goal is not find in L = " , L)

        else:
            while counter != L:

                ## برای جلوگیری از طولانی شدن خروجی پرینت های زیر کامنت شدند
                
                # print('\n************************************************************')
                # print('Frontier = {')
                # for x in frontier:
                #     print ( x.state)
                # print ('}')
                # print ('\nexpelored = ' , explored) 

                if frontier is None:
                    print ("goal is not find in L = " , L)
         
                n = frontier.pop()
                print ('\n' , n.state , ' is poped')
                if (n.state == [15,30]):
                    print ("This node is goal :)))) and goal is find in L = " , L)
                    return n
                
                if ((maze[n.state[0] - 1][n.state[1]] == '1') and ([n.state[0] - 1, n.state[1]] not in explored)):
                    child = Node ([n.state[0] - 1 , n.state[1]] , n , n.depth + 1)
                    frontier.append(child)

                if ((maze[n.state[0] + 1][n.state[1]] == '1') and ([n.state[0] + 1 , n.state[1]] not in explored)):
                    child = Node ([n.state[0] + 1 , n.state[1]] , n , n.depth + 1)
                    frontier.append(child)

                if ((maze[n.state[0]][n.state[1] - 1] == '1') and (n.state != [15,0]) and ([n.state[0] , n.state[1] - 1] not in explored)):
                    child = Node ([n.state[0] , n.state[1] - 1] , n , n.depth + 1)
                    frontier.append(child)
                
                if ((maze[n.state[0]][n.state[1] + 1] == '1') and ([n.state[0] , n.state[1] + 1] not in explored)):
                    child = Node ([n.state[0] , n.state[1] + 1] , n , n.depth + 1)
                    frontier.append(child)
     
                explored.append(n.state)
                counter += 1

goal = IDS()  
    
direction = [goal.state]
goal_parent = goal
while ([15,0] not in direction):
    goal_parent = goal_parent.parent
    direction.append(goal_parent.state)

print('Goal direction = {')

direction.reverse()
for x in direction:
    print (x)
print('}')
