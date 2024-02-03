##########################################################
# Name: Abanoub Youssef
# seria B grup 6
#Fundmental Algorthims
# assignment 9
###########################################################


import random
import time
import matplotlib.pyplot as plt

class DisjointSetNode:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0  # Initial rank is 0

def make_set(x):
    assignments_count=0
    assignments_count += 1
    return DisjointSetNode(x),assignments_count

def find_set(x):
    comparisons_count=0
    if x != x.parent:
        comparisons_count += 1
        x.parent = find_set(x.parent)  # Path compression
        
    return x.parent, comparisons_count

def union(x, y):
    compar_count=0
    assign_count=0
    
    root_x, comparisons_count1 = find_set(x)
    root_y, comparisons_count2 = find_set(y)
    
    compar_count = comparisons_count1 + comparisons_count2
    
    if root_x != root_y:
        compar_count += 1
        if root_x.rank > root_y.rank:
            assign_count += 1
            root_y.parent = root_x
            
        elif root_x.rank < root_y.rank:
            assign_count += 1
            root_x.parent = root_y
            
        else:
            assign_count += 2
            root_y.parent = root_x
            root_x.rank += 1  # Increment rank only if both trees have the same rank
            
    return  compar_count + assign_count    

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

def kruskal(graph):
    sorted_edges = sorted(graph, key=lambda edge: edge.weight)
    operationMakeset=0
    operationFindset=0
    operationUoin=0
    minimum_spanning_tree = []
    for edge in sorted_edges:
        set_edge_src,oper1 = make_set(edge.src)
        set_edge_dest, oper2 = make_set(edge.dest)
        operationMakeset +=oper1
        operationMakeset +=oper2
        if find_set(set_edge_src) != find_set(set_edge_dest):
            operationFindset +=1
            minimum_spanning_tree.append(edge)
            oper3 = union(set_edge_src, set_edge_dest)
            operationUoin +=oper3

    return minimum_spanning_tree, operationMakeset,operationFindset,operationUoin, operationUoin+operationFindset+operationMakeset

def generate_random_graph(n):
    # Ensure the graph is connected by creating a random spanning tree
    nodes = list(range(1, n + 1))  # Create a list of nodes from 1 to n
    edges = []  # Initialize an empty list to store edges of the graph
    
    # Loop to create a random spanning tree
    for i in range(2, n + 1):
        weight = random.randint(1, 100)  # Generate a random weight for the edge
        edges.append(Edge(random.choice(nodes[:i - 1]), i, weight))  # Add an edge to form a spanning tree
    
    # Add additional random edges to make the graph connected and undirected
    for _ in range(n * 4 - (n - 1)):
        src, dest = random.sample(nodes, 2)  # Choose two random nodes
        weight = random.randint(1, 100)  # Generate a random weight for the edge
        edges.append(Edge(src, dest, weight))  # Add the random edge to the graph
    
    return edges  # Return the list of edges representing the random graph


def evaluate_computational_effort(n_values):
    results = []
    for n in n_values:
        graph = generate_random_graph(n)
        
        start_time = time.time()
        minimum_spanning_tree, operationMakeset,operationFindset,operationUoin, operations = kruskal(graph)
        end_time = time.time()
        
        print(f"Number of nodes (n): {n}")
        print(f"Computational effort (comparisons + assignments): {operations}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        print()
        
        results.append(
            {
                'n': n,
                'operationMakeset': operationMakeset,
                'operationFindset': operationFindset,
                'operationUoin': operationUoin,
                'operations': operations,
                
                }
            )

    return results

def plot_results(results):
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.plot([result['n'] for result in results], [result['operationMakeset'] for result in results])
    plt.title('make set operation')
    plt.xlabel('Number of Nodes (n)')
    plt.ylabel('Computational Effort')
    
    
    plt.subplot(2, 2, 2)
    plt.plot([result['n'] for result in results], [result['operationFindset'] for result in results])
    plt.title('find operation')
    plt.xlabel('Number of Nodes (n)')
    plt.ylabel('Computational Effort')
    
    plt.subplot(2, 2, 3)
    plt.plot([result['n'] for result in results], [result['operationUoin'] for result in results])
    plt.title('uioin operation')
    plt.xlabel('Number of Nodes (n)')
    plt.ylabel('Computational Effort')

    plt.subplot(2, 2, 4)
    plt.plot([result['n'] for result in results], [result['operations'] for result in results])
    plt.title('Ttotal opertoions')
    plt.xlabel('Number of Nodes (n)')
    plt.ylabel('Computational Effort')
    

    plt.tight_layout()
    plt.savefig('chart.png')
    plt.show()

# Vary n from 100 to 10000 with step 100
n_values = list(range(100, 10001, 100))
results = evaluate_computational_effort(n_values)
plot_results(results)



# 1. **Computational Effort vs. Number of Nodes (n):**
#    - The computational effort, measured in comparisons and assignments, shows a linear relationshipwith the number of nodes (n). 
# This indicates that the algorithm's complexity is proportional to the size of the input data (number of nodes).

# 2. **Time Complexity:**
#    - The time taken for the computations doesn't show a perfectly linear relationship with the number of nodes. 
# This suggests that the time complexity of the algorithm may not be strictly linear but could have some additional factors affecting its performance.

# 3. **Performance Fluctuations:**
#    - There are fluctuations in the time taken for some consecutive values of n. 
# These fluctuations could be attributed to various factors such as system load, background processes, 
# or other external factors that might impact the execution time.

# 4. **Optimization Considerations:**
#    - It's essential to investigate the cause of any spikes or irregularities in the time taken. 
# Optimization opportunities might exist to make the algorithm more efficient and consistent, 
# ensuring that it performs well under various conditions.

# 5. **Scalability:**
#    - The performance of the algorithm seems to scale reasonably well as the number of nodes increases. However, 
# understanding the algorithm's scalability is crucial for handling larger datasets efficiently.

# 6. **Possible Influencing Factors:**
#    - The performance of the algorithm may be influenced by the specific characteristics of the input data, 
# hardware specifications, or the implementation details. A more in-depth analysis could involve profiling 
# the code and identifying potential bottlenecks.

# 7. **Improvement Strategies:**
#    - Based on the observed fluctuations and overall performance, consider exploring strategies for optimization, 
# parallelization, or algorithmic improvements to enhance the efficiency of the program.

# 8. **Conclusion:**
#    - The algorithm demonstrates a certain level of efficiency, but there is room for improvement. 
# Further investigation into the code, profiling, and optimization efforts could lead to enhanced performance, 
# making the algorithm more robust and scalable.

# Remember, these interpretations are based on the information provided. Additional details about the algorithm and 
# its implementation would be necessary for a more precise analysis and optimization recommendations.
