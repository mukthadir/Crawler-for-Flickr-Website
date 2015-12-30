__author__ = 'hchou006'

import networkx as nx
import heapq


# this method calculates the local clustering coefficient of the graph and saves it into a output file
def computeLocalClustering(graph):
    local_clustering_values = nx.clustering(graph)
    sum = 0
    counter = 0
    for values in local_clustering_values:
        sum += local_clustering_values[values]
        counter += 1
    average_local_clustering = sum/counter
    outputFile = '/Users/hchou006/Desktop/AverageLocalClustering.txt'
    file = open(outputFile, 'w')
    file.write('Average Local Clustering coefficient of the obtained graph is ' + str(average_local_clustering))
    file.close()


# this method calculates the global clustering coefficient of the graph and saves it into a output file
def computeGlobalClustering(graph):
    average_global_clustering = nx.average_clustering(graph)
    outputFile = '/Users/hchou006/Desktop/AverageGlobalClustering.txt'
    file = open(outputFile, 'w')
    file.write('Average Global Clustering coefficient of the obtained graph is ' + str(average_global_clustering))
    file.close()


# this method calculates the page rank of the top 10 nodes of the graph and saves it into a output file
def computePageRank(graph):
    pagerank = nx.pagerank(graph, alpha = 0.85)
    nodes_max_pagerank = heapq.nlargest(10, pagerank, key=pagerank.get)
    outputFile = '/Users/hchou006/Desktop/Top10PageRankValues.txt'
    file = open(outputFile, 'w')
    for nodes in nodes_max_pagerank:
       file.write('Node number = ' + str(nodes) + '     PageRank Value = ' + str(pagerank[nodes]) + '\n')
    file.close()


# this method calculates the eigen vector centrality of the top 10 nodes of the graph and saves it
# into a output file
def computeEigenVectorCentrality(graph):
    reverse_graph = graph.reverse()
    eigen_vector_centrality = nx.eigenvector_centrality(reverse_graph)
    nodes_max_eigenvector_value = heapq.nlargest(10, eigen_vector_centrality, key=eigen_vector_centrality.get)
    outputFile = '/Users/hchou006/Desktop/Top10EigenVectorValues.txt'
    file = open(outputFile, 'w')
    for nodes in nodes_max_eigenvector_value:
       file.write('Node number = ' + str(nodes) + '     EigenVector Value = ' + str(eigen_vector_centrality[nodes]) + '\n')
    file.close()


# this method calculates the degree centrality of the top 10 nodes of the graph and
# saves it into a output file
def computeCentrality(graph):
    degree_centrality = nx.degree_centrality(graph)
    nodes_max_degree_centrality = heapq.nlargest(10, degree_centrality, key=degree_centrality.get)
    outputFile = '/Users/hchou006/Desktop/Top10DegreeCentralityValues.txt'
    file = open(outputFile, 'w')
    for nodes in nodes_max_degree_centrality:
       file.write('Node number = ' + str(nodes) + '     Degree Centrality Value = ' + str(degree_centrality[nodes]) + '\n')
    file.close()


# this method calculates the maximum similarity between the two nodes and saves those two nodes
# and the corresponding maximum jaccard simimlarity value.
def computeSimilarity(graph):
    jacard_pair = nx.jaccard_coefficient(graph)
    outputFile = '/Users/hchou006/Desktop/MostSimilarNodes.txt'
    file = open(outputFile, 'w')
    nodes_max_similarity = heapq.nlargest(1, jacard_pair, key=jacard_pair.get(2))
    file.write('Node1 = ' + str(nodes_max_similarity[0]) + '     Node2 = ' + str(nodes_max_similarity[1]) + '     JaccardSimilarityValue = ' + str(nodes_max_similarity[2]) + '\n')
    file.close()


# This is the input edge list file
edgelist_file = 'AnonymizedDataset.csv'

# graph is created using the input edge list file
G = nx.read_edgelist(edgelist_file, create_using=nx.DiGraph())
undirectedG = G.to_undirected()


# we call the methods one by one to calculate all the network measures
computeLocalClustering(undirectedG)
computeGlobalClustering(undirectedG)
computePageRank(G)
computeEigenVectorCentrality(G)
computeCentrality(G)
computeSimilarity(undirectedG)
