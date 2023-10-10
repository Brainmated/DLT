'''
Question: In the missionaries and cannibals problem, 
three missionaries and three cannibals must cross a river using a boat which can carry at most two people, 
under the constraint that, for both banks, if there are missionaries present on the bank, 
they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). 
The boat cannot cross the river by itself with no people on board.
'''

path = [] #the stack

#boat = True, boat could be a boolean with True being the left, False the right

leftMiss = 3 #initial state of missionaries
rightMiss = 0 #end state of missionaries
mb = 0 #missionaries on boat

leftCann = 3
rightCann = 0
cb = 0

initial_state = (3, 3, 1) #3 missionaries, 3 cannibals and the boat to the left 
end_state = (0, 0, 0) #0 miss, 0 canns to the left, boat not to the left
moves = [(1, 0), (0, 1), (2, 0), (0, 2)]
boat = ["Left", "Right"]
side = []
visited = {} #make a queue for the visited nodes

print("Variables set.")

def get_valid_move(self, missionaries, cannibals):
    print("Valid move Found.")
    return (0 <= missionaries <= 3) and (0 <= cannibals <= 3)

def init_state(missionaries, cannibals, side):
    print("Initial state set.")
    return (missionaries, cannibals, side) == initial_state

def goal_state(missionaries, cannibals, side):
    print("Goal state set.")
    return (missionaries, cannibals, side) == goal_state

def dfs(state):
    path.append(state) #add the current state to the path
    #this will recurse until the end path is found
    if state == goal_state:
        return True
    visited[state] = True #marks the current state as visited

    #To get the current state information
    leftMiss, leftCann, boat_side = state
    print("Goal state set")

    #Iterate through all possible moves
    for move in moves:
        mb, cb = move

        if (boat_side == "Right" and rightCann <= leftCann and rightMiss <= leftMiss) or 
        (boat_side == "Left" and rightCann >= leftCann and rightMiss >= leftMiss):
        #basically generate the new state if the move is valid
        new_state = new_state #dont know how to implement this

        #Then check if the new state is not visited
        if get_valid_move(new_state) and new_state not in visited:
            #perform reccursion in the with the dfs method
            dfs(new_state)
    path.pop() #remove the last current state each time if it doesnt provide the solution

init_state(initial_state)

if dfs(init_state):
    print("Path: ", path)
