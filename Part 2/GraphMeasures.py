__author__ = 'hchou006'

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw

# This function plots the indegree/outdegree distribution
def plot(data, filename, degreetype):
    # Plot Distribution
    plt.plot(range(len(data)),data,'bo')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Count')
    plt.xlabel('In-Degree')
    plt.savefig(filename + '_' + degreetype + '_distribution.eps')
    plt.clf()


# This function finds the power-law exponent value and then saves it into a file inside the same folder
def findPowerLawExponent(degree_sequence):
    results = powerlaw.Fit(degree_sequence)
    exponent = results.power_law.alpha
    outputFile = 'PowerLawExponentValue.txt'
    file = open(outputFile, 'w')
    file.write('The power-law exponent for the obtained graph is ' + str(exponent))
    file.close()


# This function counts all the bridges that are present in the graph and then saves the
# value in an output file in the same folder
def bridge_count(undirected):
    bridge_count_number = 0
    n = nx.number_connected_components(undirected)
    for edge in undirected.edges():
        if len(set(undirected.neighbors(edge[0])) & set(undirected.neighbors(edge[1]))) == 0:
            undirected.remove_edge(edge[0], edge[1])
            if nx.number_connected_components(undirected) > n:
                bridge_count_number += 1
                print bridge_count_number
        undirected.add_edge(edge[0], edge[1])

    outputFile = 'BridgeCount.txt'
    file = open(outputFile, 'w')
    file.write('The number of bridge counts for the obtained graph is ' + str(bridge_count_number))
    file.close()

# This function counts the number of three cycles that are present in the graph and then
# saves the value in an output file in the same folder.
def count_three_cycles(undirected):
    number_of_three_cycles = 0

    visited_ids = set()
    for node_a_id in undirected:
        for node_b_id in undirected[node_a_id]:
            if node_b_id in visited_ids:
                continue
            for node_c_id in undirected[node_b_id]:
                if node_c_id in visited_ids:
                    continue
                if node_a_id in undirected[node_c_id]:
                    number_of_three_cycles+=1
        visited_ids.add(node_a_id)
    outputFile = 'ThreeCycles.txt'
    file = open(outputFile, 'w')
    file.write('The number of Three cycles in the obtained graph is ' + str(number_of_three_cycles))
    file.close()


# This function calculates the diameter of the graph. Since the graph is very large,
# it takes a lot of time to calculate and save the value in a output file.
def diameter(undirected):
    dia = nx.diameter(undirected)
    outputFile = 'Diameter.txt'
    file = open(outputFile, 'w')
    file.write('The diameter of the obtained graph is ' + str(dia))
    file.close()


# Take the edgelist file as input
edgelist_file = 'AnonymizedDataset.csv'

# Prepare graph from input edge-list
G = nx.read_edgelist(edgelist_file, create_using=nx.DiGraph())

# reverse the graph edge directions.
reverse = nx.reverse(G)

# Prepare sparse adjacency matrix
matrix = nx.to_scipy_sparse_matrix(G)

# this get the adjacency matrix for the reversed graph
revM = nx.to_scipy_sparse_matrix(reverse)

# this calculates the indegrees of the graph
indegrees = matrix.sum(0).A[0]
indegree_distribution = np.bincount(indegrees)

outdegrees = revM.sum(0).A[0]
outdegree_distribution = np.bincount(outdegrees)

# get the degree sequence of all the nodes
degree_sequence=nx.degree(G).values()

# Convert directed graph into undirected graph
undirected = G.to_undirected(G)


# Here, we call all the functions one by one to get the corresponding values
plot(indegree_distribution, edgelist_file, 'indegree')
#plot(outdegree_distribution, edgelist_file, 'outdegree')
findPowerLawExponent(degree_sequence)
bridge_count(undirected)
count_three_cycles(undirected)
diameter(undirected)
