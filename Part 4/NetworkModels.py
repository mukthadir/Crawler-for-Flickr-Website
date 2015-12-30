__author__ = 'hchou006'

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import heapq


# I am generating a random graph with the same number of nodes and edges as I obtained in the original graph.
randomGraph = nx.dense_gnm_random_graph(213006,676575)

# I am generating a small world model with the same number of nodes as I obtained in the original graph.
smallWorldGraph = nx.connected_watts_strogatz_graph(213006, 3, 0.45, 10000)

# I am generating a preferential attachment model with the same number of nodes
# as I obtained in the original graph.
preferential_model = nx.barabasi_albert_graph(213006,4)


# this method finds the average path length of the given graph
def averagePathLength(graph, filename):
    length = nx.average_shortest_path_length(graph)
    outputFile = "/Users/hchou006/Desktop/{0}.txt".format(filename)
    file = open(outputFile, 'w')
    file.write('Average path length of the obtained graph is ' + str(length))
    file.close()


# this method finds the local clustering coefficient of the given graph
def computeLocalClustering(graph, filename):
    local_clustering_values = nx.clustering(graph)
    sum = 0
    counter = 0
    for values in local_clustering_values:
        sum += local_clustering_values[values]
        counter += 1
    average_local_clustering = sum/(sum + counter)
    outputFile = "/Users/hchou006/Desktop/{0}.txt".format(filename)
    file = open(outputFile, 'w')
    file.write('Average Local Clustering coefficient of the obtained graph is ' + str(average_local_clustering))
    file.close()


# this method finds the global clustering coefficient of the given graph
def computeGlobalClustering(graph, filename):
    average_global_clustering = nx.average_clustering(graph)
    outputFile = "/Users/hchou006/Desktop/{0}.txt".format(filename)
    file = open(outputFile, 'w')
    file.write('Average Global Clustering coefficient of the obtained graph is ' + str(average_global_clustering))
    file.close()


# this method computes the page rank of the top 10 nodes of the given graph
def computePageRank(graph):
    pagerank = nx.pagerank(graph, alpha = 0.85)
    nodes_max_pagerank = heapq.nlargest(10, pagerank, key=pagerank.get)
    outputFile = "/Users/hchou006/Desktop/{0}.txt".format(filename)
    file = open(outputFile, 'w')
    for nodes in nodes_max_pagerank:
       file.write('Node number = ' + str(nodes) + '     PageRank Value = ' + str(pagerank[nodes]) + '\n')
    file.close()


# this method computes the degree centrality of the top 10 nodes of the given graph
def computeCentrality(graph, filename):
    degree_centrality = nx.degree_centrality(graph)
    nodes_max_degree_centrality = heapq.nlargest(10, degree_centrality, key=degree_centrality.get)
    outputFile = "/Users/hchou006/Desktop/{0}.txt".format(filename)
    file = open(outputFile, 'w')
    for nodes in nodes_max_degree_centrality:
       file.write('Node number = ' + str(nodes) + '     Degree Centrality Value = ' + str(degree_centrality[nodes]) + '\n')
    file.close()


# this method plots the degree distribution of the given graph
def plot(graph, degreetype, filename):
    M = nx.to_scipy_sparse_matrix(graph)

    indegrees = M.sum(0).A[0]
    indegree_distribution = np.bincount(indegrees)

    # Plot Distribution
    plt.plot(range(len(indegree_distribution)),indegree_distribution,'bo')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Count')
    plt.xlabel('In-Degree')
    plt.savefig(degreetype + "_distribution_{0}.eps".format(filename))
    plt.clf()


# here we calculate all the different values for the random graph
filename = 'randomGraph'
plot(randomGraph, 'indegree', filename)
filename = 'AverageLocalClusteringRandomGraph'
computeLocalClustering(randomGraph, filename)
filename = 'AverageGlobalClusteringRandomGraph'
computeGlobalClustering(randomGraph, filename)
filename = 'Top10DegreeCentralityValuesRandomGraph'
computeCentrality(randomGraph, filename)
filename = 'Top10PageRankValuesRandomGraph'
computePageRank(randomGraph, filename)


# here we calculate all the different values for the small world graph
filename = 'smallWorldGraph'
plot(smallWorldGraph, 'indegree', filename)
filename = 'AverageLocalClusteringsmallWorldGraph'
computeLocalClustering(smallWorldGraph, filename)
filename = 'AverageGlobalClusteringsmallWorldGraph'
computeGlobalClustering(smallWorldGraph, filename)
filename = 'Top10DegreeCentralityValuessmallWorldGraph'
computeCentrality(smallWorldGraph, filename)
filename = 'Top10PageRankValuessmallWorldGraph'
computePageRank(smallWorldGraph, filename)


# here we calculate all the different values for the preferential attachment model
filename = 'PrefAttachModel'
plot(preferential_model, 'indegree', filename)
filename = 'AverageLocalClusteringPrefAttachModel'
computeLocalClustering(preferential_model, filename)
filename = 'AverageGlobalClusteringPrefAttachModel'
computeGlobalClustering(preferential_model, filename)
filename = 'Top10DegreeCentralityValuesPrefAttachModel'
computeCentrality(preferential_model, filename)
filename = 'Top10PageRankValuesPrefAttachModel'
computePageRank(preferential_model, filename)


# average path length calculation takes a lot of time and hence I am calculating them
# at the end
filename = 'AveragePathLengthRandomGraph'
averagePathLength(randomGraph, filename)

filename = 'AveragePathLengthsmallWorldGraph'
averagePathLength(smallWorldGraph, filename)

filename = 'AveragePathLengthPrefAttachModel'
averagePathLength(preferential_model, filename)