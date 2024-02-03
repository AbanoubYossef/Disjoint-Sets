# Kruskal's Algorithm Computational Effort Analysis

## Overview
This repository contains an implementation of Kruskal's algorithm for finding the minimum spanning tree of a graph. The primary focus is on analyzing the computational effort in terms of comparisons and assignments for different input sizes (number of nodes).

## Contents
- `kruskal_algorithm.py`: Python script containing the implementation of Kruskal's algorithm.
- `README.md`: This documentation file providing an overview, usage instructions, and analysis of the algorithm's performance.
- `chart.png`: A chart illustrating the computational effort for different input sizes.

## Usage
1. Run the `kruskal_algorithm.py` script to execute the algorithm and generate computational effort data.
2. The script will output information about the number of nodes, comparisons, assignments, and total operations.
3. The results will be plotted and saved as `chart.png` for visual analysis.

## Computational Effort Analysis
The computational effort is measured in terms of comparisons and assignments. The analysis includes the following components:
1. **make set operation**: The computational effort of creating a disjoint set.
2. **find operation**: The computational effort of finding the representative of a set using path compression.
3. **union operation**: The computational effort of merging two sets.

## Results
The script evaluates the computational effort for various input sizes (number of nodes) and produces a chart (`chart.png`) to visualize the performance trends.

## Observations
1. **Computational Effort vs. Number of Nodes (n):**
   - The computational effort shows a linear relationship with the number of nodes, indicating a proportional complexity.

2. **Time Complexity:**
   - The time taken for computations exhibits fluctuations but generally scales with the number of nodes.

3. **Performance Fluctuations:**
   - Fluctuations in time may be influenced by external factors; further investigation is recommended.

4. **Optimization Considerations:**
   - Explore optimization opportunities for more efficient and consistent performance.

5. **Scalability:**
   - The algorithm scales reasonably well, but scalability considerations are crucial for larger datasets.

6. **Possible Influencing Factors:**
   - Factors like input characteristics, hardware, or implementation details may influence performance.

7. **Improvement Strategies:**
   - Profiling and optimization efforts could enhance algorithm efficiency and scalability.

8. **Conclusion:**
   - The algorithm is efficient, but further optimization could improve robustness and scalability.

## Contributors
- Abanoub Youssef (Author)

Feel free to explore and contribute to enhance the analysis and overall codebase.
