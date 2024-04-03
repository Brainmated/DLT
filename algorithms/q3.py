import heapq
import sys
import time

def dijkstra(graph, cleared_villages, start_village):
    distances = {village: float('inf') for village in graph}
    distances[start_village] = 0
    #set the initial node as the start node in the priority queue
    pq = [(0, start_village)]

    #loop until the priority queue is empty
    while pq:
        current_dist, current_village = heapq.heappop(pq)
        #if the current distance is greater than the distance of the current village, skip
        if current_dist > distances[current_village]:
            continue
        #loop through the neighbors of the current village and update the distance if the new distance is less than the current distance
        for neighbor, clear_cost, traverse_cost in graph[current_village]:
            if neighbor in cleared_villages:
                continue
            #calculate the new distance to the neighbor village
            new_dist = current_dist + traverse_cost
            #if the new distance is less than the current distance, update the distance and push the new distance to the priority queue
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

def construct_road_network(graph):
    cleared_villages = set()
    total_cost = 0
    #keep track of the sequence of cleared roads
    road_sequence = []  

    #choose the initial village (with the smallest clearing cost)
    starting_village = min((roads[0][1], village) for village, roads in graph.items())[1]
    #append the initial village to the cleared villages
    cleared_villages.add(starting_village)

    #loop until all villages are cleared
    while len(cleared_villages) < len(graph):
        cheapest_road = None
        cheapest_cost = float('inf')
        #cheap road is the road with the smallest cost to clear
        for cleared_village in cleared_villages:

            distances = dijkstra(graph, cleared_villages, cleared_village)
            for neighbor, clear_cost, traverse_cost in graph[cleared_village]:
                if neighbor in cleared_villages:
                    continue
                cost = distances[neighbor] + clear_cost
                if cost < cheapest_cost:
                    cheapest_cost = cost
                    cheapest_road = (cleared_village, neighbor, clear_cost, traverse_cost)

        #raise error in case of disconnected graph or invalid input
        if cheapest_road is None:
            raise ValueError("No valid road found. The graph might be disconnected.")

        #update the true total cost
        #hope the clear cost is the 3rd element
        total_cost += cheapest_road[2]
        cleared_villages.add(cheapest_road[1])
        #append the cheapest road to the sequence
        road_sequence.append(cheapest_road)  

    return total_cost, road_sequence

def parse_input(file):

    graph = {}
    num_villages = int(next(file).strip())

    #construct the graph
    for _ in range(num_villages):
        line = next(file).strip()
        parts = line.split()
        
        #first element is the village name
        a = parts[0]
        #loop through the neighbors of the village
        for i in range(1, len(parts), 3):
            b = parts[i]
            clear_cost = int(parts[i+1])
            traverse_cost = int(parts[i+2])
            #add the neighbor to the village network
            if a not in graph:
                #initialize the village with an empty list
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, clear_cost, traverse_cost))
            #in case of undirected graph
            graph[b].append((a, clear_cost, traverse_cost))  
    return graph

def main():
    #ONLY FOR .TXT FILE
    graph = parse_input(sys.stdin)
    total_cost, road_sequence = construct_road_network(graph)

    print("Sequence of cleared roads:")
    for road in road_sequence:
        print(f"{road[0]} -> {road[1]} (Clearing Cost: {road[2]}, Traverse Cost: {road[3]})")
    print("Total minimum cost to clear roads and connect all villages:", total_cost)

if __name__ == "__main__":
    main()

'''Test case 1:
52
a B 2 3 c 1 5
b C 4 1 a 1 5 D 3 2
c d 2 3 b 3 2 e 1 4
d E 5 1 c 1 4 f 2 3
e F 3 2 d 2 3 g 4 1
f G 1 5 e 4 1 h 2 2
g H 4 1 f 2 2 i 3 4
h I 2 3 g 3 4 j 1 5
i J 5 2 h 1 5 k 4 1
j K 1 4 i 4 1 l 3 3
k L 2 2 j 3 3 m 5 1
l M 4 3 k 5 1 n 1 2
m N 1 5 l 1 2 o 2 4
n O 3 1 m 2 4 p 4 3
o P 2 2 n 4 3 q 5 1
p Q 5 3 o 5 1 r 1 4
q R 1 2 p 1 4 s 3 5
r S 4 1 q 3 5 t 2 2
s T 2 4 r 2 2 u 1 3
t U 3 5 s 1 3 v 5 1
u V 1 2 t 5 1 w 4 3
v W 3 1 u 4 3 x 2 4
w X 2 2 v 2 4 y 1 5
x Y 4 5 w 1 2 z 3 1
y Z 5 4 x 4 5 a 2 3
z A 1 3 y 5 4 b 3 2
A B 2 3 Z 1 5
B C 4 1 A 1 5 D 3 2
C D 2 3 B 3 2 E 1 4
D E 5 1 C 1 4 F 2 3
E F 3 2 D 2 3 G 4 1
F G 1 5 E 4 1 H 2 2
G H 4 1 F 2 2 I 3 4
H I 2 3 G 3 4 J 1 5
I J 5 2 H 1 5 K 4 1
J K 1 4 I 4 1 L 3 3
K L 2 2 J 3 3 M 5 1
L M 4 3 K 5 1 N 1 2
M N 1 5 L 1 2 O 2 4
N O 3 1 M 2 4 P 4 3
O P 2 2 N 4 3 Q 5 1
P Q 5 3 O 5 1 R 1 4
Q R 1 2 P 1 4 S 3 5
R S 4 1 Q 3 5 T 2 2
S T 2 4 R 2 2 U 1 3
T U 3 5 S 1 3 V 5 1
U V 1 2 T 5 1 W 4 3
V W 3 1 U 4 3 X 2 4
W X 2 2 V 2 4 Y 1 5
X Y 4 5 W 1 2 Z 3 1
Y Z 5 4 X 4 5 A 2 3
Z a 1 3 Y 5 4 b 3 2
'''