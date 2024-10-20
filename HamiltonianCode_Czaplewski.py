# -*- coding: utf-8 -*-
"""HamiltonianCode_Czaplewski

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CbMOhm0IhXihjqkFLX16C80NhXtRT0Nf
"""

import networkx as nx
import numpy as np
import itertools
import time
import matplotlib.pyplot as plt

def random_graph(num_vertices, edge_probability=0.5):
    """
    Creates a random graph using NetworkX and converts it to an adjacency matrix.
    """
    G = nx.gnp_random_graph(num_vertices, edge_probability)
    adj_matrix = nx.to_numpy_array(G, dtype=int)
    return adj_matrix

def is_hamiltonian_cycle(graph, path):
    """
    Checks if a given path is a Hamiltonian cycle.
    """
    return len(path) == len(graph) and all(graph[path[i - 1]][path[i]] for i in range(len(path)))

def find_hamiltonian_cycle(graph):
    """
    Tries to find a Hamiltonian cycle by checking all permutations.
    Returns the cycle if found, otherwise None.
    """
    n = len(graph)
    for perm in itertools.permutations(range(n)):
        if is_hamiltonian_cycle(graph, perm):
            return perm  # Found a Hamiltonian cycle
    return None

def main():
    sizes = range(4, 11)  # Vertex sizes from 4 to 10
    trials_per_size = 50  # 50 trials per vertex size

    cycles_found = {size: [] for size in sizes}  # Store found cycles per size
    avg_execution_times = []  # Store average execution times per size
    all_execution_times = []  # Store all times for plotting

    print("Random Hamiltonian Path Test:")

    for size in sizes:
        execution_times = []  # Store execution times for this size

        for _ in range(trials_per_size):
            graph = random_graph(size, edge_probability=0.5)

            start_time = time.perf_counter()  # Use high-resolution timer
            cycle = find_hamiltonian_cycle(graph)
            exec_time = time.perf_counter() - start_time  # Measure execution time

            execution_times.append(exec_time)
            all_execution_times.append((size, exec_time))  # Collect data for plotting

            if cycle:
                cycles_found[size].append(cycle)

        # Calculate and store average execution time for this size
        avg_time = np.mean(execution_times)
        avg_execution_times.append(avg_time)

        # Output average execution time for the current size
        print(f"Size {size} Execution time: {avg_time:.4f} seconds avg.")

    # Output all found Hamiltonian cycles
    print("\nA Hamiltonian Cycles Found:")
    for size, cycles in cycles_found.items():
        print(f"Size {size}: {cycles if cycles else 'None'}")

    # Plotting the performance graph
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot individual execution times as green dots with 1.0 y-axis scale
    sizes_list, times_list = zip(*all_execution_times)
    ax1.scatter(sizes_list, times_list, color='green', alpha=0.6, label='Execution Time (Points)')
    ax1.set_ylabel('Execution Time (seconds)', color='green')
    ax1.set_xlabel('Number of Vertices')
    ax1.tick_params(axis='y', labelcolor='green')
    ax1.set_yticks(np.arange(0, int(max(times_list)) + 2, 1))  # Y-axis for individual points with scale of 1.0

    # Create second y-axis for average execution times with 0.1 y-axis scale
    ax2 = ax1.twinx()
    ax2.plot(sizes, avg_execution_times, color='blue', label='Average Execution Time', linewidth=2)
    ax2.scatter(sizes, avg_execution_times, color='blue', marker='o')  # Points on the line
    ax2.set_ylabel('Average Execution Time (seconds)', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.set_yticks(np.arange(0, max(avg_execution_times) + 0.2, 0.1))  # Y-axis for average time with scale of 0.1

    # Set plot title
    plt.title('Performance of Hamiltonian Cycle Data')

    fig.tight_layout()  # Ensures the layout is not overlapping
    plt.show()

if __name__ == "__main__":
    main()