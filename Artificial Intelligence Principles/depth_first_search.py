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

visited = set() #a set to add each visited node
stack = []

def depth_first_search(visited, graph, node):
    #check if the node is not visited
    if node not in visited:
        #add the visited node to the set
        visited.add(node)
        print(node)
        #for each neighbour found for the next node, perform recursion: dfs(visited, graph, 'neighbouring node')
        for neighbour in graph[node]:
            depth_first_search(visited, graph, neighbour)

depth_first_search(visited, graph, 'A')
