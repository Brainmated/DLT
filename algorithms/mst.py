def parse_input(input_lines):
    edges = []
    # Iterate over each line after the first line
    for line in input_lines[1:]:
        parts = line.split()
        node1 = parts[0]
        # Iterate over the nodes and costs (skip the '0's which are not needed)
        for i in range(1, len(parts), 3):
            node2 = parts[i]
            cost = int(parts[i + 1])
            edges.append((cost, node1, node2))
    return edges

def kruskal(nodes, edges):
    edges.sort()
    parent = {node: node for node in nodes}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1

    MST = []
    total_cost = 0
    for cost, node1, node2 in edges:
        if find(node1) != find(node2):
            union(node1, node2)
            MST.append((node1, node2, cost))  # Store the edge with its cost
            total_cost += cost
            if len(MST) == len(nodes) - 1:
                break
    
    return MST, total_cost

# Read the number of nodes
N = int(input())

# Read the connections and their costs
input_lines = [input() for _ in range(N)]

# Parse the input to get the edges
edges = parse_input(input_lines)

# Extract a set of nodes from the edges
nodes = set()
for edge in edges:
    nodes.update([edge[1], edge[2]])

# Find the MST and total cost
MST, total_cost = kruskal(nodes, edges)

# Output the edges in the MST and the total cost
for node1, node2, cost in MST:  
    print(f"From: {node1} to: {node2} | cost: {cost}")  # Print the edge and its cost
print(f"Total minimum cost: {total_cost}")
