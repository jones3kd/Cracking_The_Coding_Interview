""" only use ints for these values


Problem Statement

Given an undirected graph consisting of N nodes (labelled 1 to N) where a specific given node S represents the start position and an edge between any two nodes is of length 6 units in the graph.

It is required to calculate the shortest distance from start position (Node S) to all of the other nodes in the graph.

Note 1: If a node is unreachable , the distance is assumed as −1.
Note 2: The length of each edge in the graph is 6 units.

Input Format

The first line contains T, denoting the number of test cases.
First line of each test case has two integers N, denoting the number of nodes in the graph and M, denoting the number of edges in the graph.
The next M lines each consist of two space separated integers x y, where x and y denote the two nodes between which the edge exists.
The last line of a testcase has an integer S, denoting the starting position.

Constraints
1≤T≤10
2≤N≤1000
1≤M≤N×(N−1)2
1≤x,y,S≤N

Output Format

For each of T test cases, print a single line consisting of N−1 space-separated integers, denoting the shortest distances of the N-1 nodes from starting position S. This will be done for all nodes same as in the order of input 1 to N.

For unreachable nodes, print −1.

Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output

6 6 -1
-1 6
Explanation

For test cases 1:

The graph given in the test case is shown as :

Graph

S denotes the node 1 in the test case and B,C and D denote 2,3 and 4. Since S is the starting node and the shortest distances from it are (1 edge, 1 edge, Infinity) to the nodes B,C and D (2,3 and 4) respectively.

Node D is unreachable, hence -1 is printed (not Infinity).

For test cases 2: There are only one edge (2, 3) in a graph with 3 nodes, so node 1 is unreachable from node 2, and node 3 has one edge from node 2, each edge has the length of 6 units. So we output -1 6.
 """
edge_len = 6
cases = input()
cases = int(cases)

while cases:
    graph = {}
    visited = {}#if not in dictionary its false and unvisited
    queue = []
    dist = {}

    line = input()
    nodes_neigh = line.split()
    nodes = nodes_neigh[0]
    nodes = int(nodes)
    #set up dictionaries
    for num in range(1, (nodes + 1)):
        graph[num] = []
        dist[num] = -1 #initiliaze distance to -1

    num_neighbors = nodes_neigh[1]
    #print(nodes)
    #print(num_neighbors)
    for num in range(int(num_neighbors)):
        line = input()
        line = line.split()
        node = int(line[0])
        adj = int(line[1])

        #print("node: %s, adj %s"%(node,adj))
        if node not in graph:
            graph[node] = []

        if adj not in graph:
            graph[adj] = []

        graph[node].append(adj)
        graph[adj].append(node)

    start_node = input()
    start_node = int(start_node)

    #start bfs
    #add root to queue
    queue.append(start_node)

    while len(queue) > 0:
        node = queue.pop(0)

        children = graph[node]

        for child in children:
            if child not in visited:
                visited[child] = True
                queue.append(child)

                if start_node == node: #start distance at 6
                    dist[child] = edge_len
                else:
                    dist[child] = dist[node] + edge_len

    for key in dist:
        #print("key: "+str(key))
        if key != start_node:
            print(str(dist[key]) + " ",end="")


    print("")
    cases -= 1
