'''
Question: In the missionaries and cannibals problem, 
three missionaries and three cannibals must cross a river using a boat which can carry at most two people, 
under the constraint that, for both banks, if there are missionaries present on the bank, 
they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). 
The boat cannot cross the river by itself with no people on board.
'''

path = [] #the stack

#boat = True, boat could be a boolean with True being the left, False the right

initial_state = (3, 3, 1) #3 missionaries, 3 cannibals and the boat to the left 
end_state = (0, 0, 0) #0 miss, 0 canns to the left, boat not to the left
moves = [(1, 0), (0, 1), (2, 0), (0, 2)]
boat = ["Left", "Right"]
side = []
visited = {}
    

def get_valid_move(self, missionaries, cannibals):

    return (0 <= missionaries <= 3) and (0 <= cannibals <= 3)

def init_state(missionaries, cannibals, side):
    return (missionaries, cannibals, side) == initial_state

def goal_state(missionaries, cannibals, side):
    return (missionaries, cannibals, side) == goal_state

def dfs(state):
    path.append(state) #add the current state to the path

    if state == goal_state:
        return True
    visited[state] = True #marks the current state as visited
