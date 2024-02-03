##########################################################
# Name: Abanoub Youssef
# seria B grup 6
#Fundmental Algorthims
#this is the demo for the task
# assignment 9
###########################################################


class DisjointSetNode:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0  # Initial rank is 0

def make_set(x):
    # Create a set with the element x
    return DisjointSetNode(x)

def find_set(x):
    # Find the set that contains the element x with path compression
    if x != x.parent:
        x.parent = find_set(x.parent)  # Path compression
    return x.parent

def union(x, y):
    # Union the sets containing elements x and y using rank
    root_x = find_set(x)
    root_y = find_set(y)

    #the smallest rank will be the child
    if root_x != root_y:
        if root_x.rank > root_y.rank:
            root_y.parent = root_x
        elif root_x.rank < root_y.rank:
            root_x.parent = root_y
        else:
            root_y.parent = root_x
            root_x.rank += 1  
            # Increment rank only if both trees have the same rank

# Example usage:
sets = [make_set(i) for i in range(10)]

# Perform UNION and FIND_SET operations
union(sets[0], sets[1])
union(sets[1], sets[3])
union(sets[3], sets[2])
print(find_set(sets[0]).key)
print(find_set(sets[1]).key)
print(find_set(sets[2]).key)
print(find_set(sets[3]).key)

print(find_set(sets[5]).key)#to know that didn't apply for this node

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def kruskal(graph):
    # Sort edges in non-decreasing order of their weight
    sorted_edges = sorted(graph, key=lambda edge: edge.weight)

    minimum_spanning_tree = []
    for edge in sorted_edges:

        # Use make_set to convert integers to DisjointSetNode
        set_edge_src = make_set(edge.src)
        set_edge_dest = make_set(edge.dest)

        if find_set(set_edge_src) != find_set(set_edge_dest):
            minimum_spanning_tree.append(edge)
            union(set_edge_src, set_edge_dest)

    return minimum_spanning_tree

# Example usage:
edges = [
    Edge(0, 1, 2), Edge(0, 2, 4), Edge(0, 3, 1),
    Edge(1, 2, 3), Edge(1, 3, 2),
    Edge(2, 3, 5), Edge(2, 4, 7), Edge(2, 5, 6),
    Edge(3, 4, 6), Edge(3, 5, 8),
    Edge(4, 5, 9), Edge(4, 6, 10), Edge(4, 7, 11),
    Edge(5, 7, 12),
    Edge(6, 7, 13)
]

# Display edges of the graph
print("Edges of the Graph:")
for edge in edges:
    print(f"Edge: {edge.src} - {edge.dest}, Weight: {edge.weight}")

# Apply Kruskal's algorithm
minimum_spanning_tree = kruskal(edges)

# Display edges in the minimum spanning tree
print("\nEdges in Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"Edge: {edge.src} - {edge.dest}, Weight: {edge.weight}")
