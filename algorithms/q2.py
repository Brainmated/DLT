import sys
import time

class DisjointSet:
    
    #initialize trhe disjoint set
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        #find the initial item
        if self.parent[item] != item:
            #recursively find the parent of the item
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def combine(self, set1, set2):
        #combine the two sets
        root1 = self.find(set1)
        root2 = self.find(set2)
        #if the roots are not the same, combine the two sets
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(vertices, edges):
    #minimum spanning tree
    mst = []
    #initial current cost
    total_cost = 0

    ds = DisjointSet(vertices)

    #sort the edges by weight
    edges.sort(key=lambda x: x[2])

    #loop through the edges
    for edge in edges:
        u, v, weight = edge
        #if the two vertices are not in the same set, combine them
        if ds.find(u) != ds.find(v):
            ds.combine(u, v)
            mst.append(edge)
            total_cost += weight

    return mst, total_cost

def parse_input(input_lines):
    edges = []
    vertices = set()
    for line in input_lines:
        parts = line.split()
        node1 = parts[0]
        vertices.add(node1)
        #loop through the neighbors of the village
        for i in range(1, len(parts) - 1, 3):
            node2 = parts[i]
            cost = int(parts[i + 1])
            #add the neighbor to the village network
            edges.append((node1, node2, cost))
            vertices.add(node2)
    return list(vertices), edges

def main():
    input_lines = sys.stdin.readlines()
    N = int(input_lines[0].strip())
    vertices, edges = parse_input(input_lines[1:])
    mst, total_cost = kruskal(vertices, edges)

    for edge in mst:
        print(f"From: {edge[0]} To: {edge[1]} | Cost: {edge[2]}")
    print(f"TOTAL COST: {total_cost}")

if __name__ == "__main__":
    main()
end_time = time.time()
print(f"Execution time: {end_time - DisjointSet.start_time}")

'''
Test case 1:

52
J d 99 0 f 41 0 i 71 0
T C 30 0 M 24 0 j 99 0
C s 83 0 t 26 0
b S 84 0 j 44 0 q 13 0
j B 48 0 C 32 0 G 39 0 M 87 0
v O 69 0 S 75 0 Y 81 0 c 48 0
N Q 74 0 Z 35 0 h 70 0 s 28 0
x C 28 0 m 13 0 r 39 0 w 27 0
w P 10 0 T 11 0 Y 66 0 u 85 0
I N 25 0 V 30 0 s 22 0
S Q 90 0 X 80 0 u 75 0
Y R 68 0 r 28 0
n P 86 0 g 58 0 t 75 0
l F 17 0 L 73 0 T 65 0 n 50 0
M C 10 0 I 67 0 e 81 0
s O 76 0 b 42 0 l 60 0
g r 40 0 y 22 0
G e 92 0 k 47 0
P X 19 0 a 27 0 k 71 0
i h 14 0 x 42 0
h b 28 0 i 33 0 j 68 0 u 97 0
V J 96 0 O 76 0
Q A 74 0 I 14 0 R 15 0 z 93 0
B H 19 0 N 61 0 a 82 0 o 93 0
p T 97 0 x 33 0
R D 84 0 o 33 0 y 31 0
X E 49 0 O 53 0 V 57 0
m Y 61 0 h 45 0 l 97 0
K I 26 0 g 67 0
q b 77 0 j 93 0 l 45 0
c L 76 0 N 42 0 P 87 0
z M 10 0 a 54 0 r 98 0
E G 59 0 l 29 0
t B 81 0 V 59 0
Z P 57 0 T 18 0 g 45 0 n 65 0
L e 97 0 f 77 0 o 52 0
u L 80 0 O 53 0
d f 35 0 k 94 0
r E 17 0 Z 61 0 c 76 0
A K 76 0 k 17 0 u 24 0
H C 77 0 Q 72 0 V 89 0 x 37 0
F N 61 0 P 77 0
W M 79 0 X 54 0
f M 56 0 d 20 0 i 91 0
y J 75 0 M 44 0 U 94 0 W 69 0
O Q 16 0 q 59 0 t 63 0
U L 80 0 o 28 0 p 34 0
a D 15 0 E 64 0 M 34 0
D K 56 0 k 28 0 l 35 0 v 22 0
k D 27 0 u 30 0
o C 20 0 a 31 0 l 33 0
e c 38 0 n 39 0

'''

'''
Test case 2:

52
m A 33 0 M 27 0
P L 41 0 V 54 0 c 99 0
t A 27 0 T 75 0 c 25 0
D T 17 0 c 59 0 e 82 0 i 33 0
O Q 88 0 d 93 0 e 86 0 f 54 0
y O 86 0 h 50 0 n 76 0 p 81 0
f I 25 0 a 37 0 o 14 0
e A 22 0 b 100 0 h 97 0 v 15 0
H V 47 0 o 33 0
s B 62 0 I 68 0
h L 90 0 N 15 0 f 44 0 r 10 0
w h 19 0 z 50 0
o K 41 0 a 19 0 e 45 0 k 58 0
z A 69 0 s 46 0
r V 85 0 a 10 0 w 100 0
j Z 30 0 e 86 0 k 93 0
U A 37 0 b 16 0 j 74 0
S h 80 0 j 18 0
x D 40 0 E 94 0 z 54 0
Q T 14 0 j 48 0 z 84 0
c D 83 0 X 14 0 r 22 0
J O 34 0 d 30 0 z 47 0
B I 60 0 K 19 0 R 86 0 n 53 0
I B 86 0 h 78 0
M Q 78 0 Y 73 0 u 57 0
v A 70 0 K 34 0 U 25 0 c 86 0
G T 56 0 c 11 0 p 39 0 s 71 0
i M 76 0 Q 46 0 q 26 0
u F 67 0 g 26 0 m 50 0 p 91 0
g H 19 0 i 79 0 n 66 0 y 21 0
W A 71 0 Z 33 0 o 85 0 z 55 0
F N 13 0 O 32 0 j 61 0 k 34 0
p D 62 0 G 54 0 n 94 0
Y F 25 0 I 12 0 s 98 0
L A 30 0 u 35 0
a b 30 0 q 45 0
d F 92 0 l 59 0
R E 40 0 N 61 0 x 32 0
l B 17 0 o 25 0
q E 48 0 H 18 0 s 58 0 w 86 0
V H 48 0 J 47 0 x 89 0
C E 41 0 M 44 0 R 64 0 V 35 0
n Q 88 0 Y 47 0
N C 72 0 j 67 0
E G 78 0 S 18 0 h 20 0
T A 67 0 B 34 0 Q 33 0 R 91 0
A E 64 0 V 91 0 q 58 0 w 26 0
b X 77 0 l 91 0 u 93 0 w 39 0
k A 100 0 z 91 0
X R 20 0 r 76 0
K D 86 0 E 97 0 g 42 0 r 50 0
Z C 89 0 E 75 0

'''