import time
#dictionary to represent the graph, each key corresponds to a node, each value corresponds to a neighbor
graph = {
    'A': ["B", "C"],
    'B': ["D", "E"],
    'C': ["F"],
    'D': [],
    'E': ["F"],
    'F': ["H"],
    'G': [], #this node doesnt exist in the graph
    'H': []
}
start_time = time.time()
visited = [] #append in this list each visited node
queue = [] #add each visited node in queue, then remove node when no more neighboring nodes

def breadth_first_search(graph, visited, node): #graph takes the graph created, visited keeps track of the visited nodes, node starts with the starting node
    visited.append(node)
    queue.append(node)

    while queue: #while queue contains elements, it removes nodes from the queue and appends the neighbors of the node if they are unvisited,
                 #marking them as visited, continues until the queue is empty
        s = queue.pop(0) #removes and returns the first element from the queue
        #pop(0) searches in a bfs manner, whereas pop() searches in depth
        print(s, end = " ") #displays the visited nodes, additionally it displays the order in which nodes are visited

        for neighbor in graph[s]: #this loop iterrates over the neighboring nodes of the current node 's'
            if neighbor not in visited: #checks if each neighbor hasnt been visited before 
                visited.append(neighbor) #adds them to the visited list
                queue.append(neighbor) #adds them to the queue list

breadth_first_search(graph, visited, 'A') #starting node set
end_time = time.time()
total_time = end_time - start_time
print("\nCompile Time: ", total_time)
