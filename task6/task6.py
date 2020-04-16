# CIS 223 | Spring 2020 | Task 6
# Author : Colin Roskos
# Implementation of Bellman-Ford shrotest path algorithm
#
# Graphs will be represented with an adjacency list:
#  e.g. G={'P':{‘Q’: 6, ’R’: 2}, ‘Q’: {‘P’:6,’R’:4}, ‘R’: {‘P’:2,’Q’,4}}
#    Read as vertex P has an edge with Q with weight '6'
#

def Bellman_Ford(Graph, startV):
    """
    Implementation of Bellman-Ford shortest path algorithm using an adjacency list.

    :param graph:
    :param s_vert:
    :return: predV and distanceDict
    """
    vertex_data = {}
    for curent_vertex in Graph:
        vertex_data[curent_vertex] = [float('inf'), 0]  # { vertex: [dist, predV] }

    vertex_data[startV][0] = 0

    for i in range(len(Graph)-1):
        for currentV in Graph:
            for adjV in Graph[currentV]:
                edgeWeight = Graph[currentV][adjV]
                alternativePathDistance = vertex_data[currentV][0] + edgeWeight

                if alternativePathDistance < vertex_data[adjV][0] :
                    vertex_data[adjV][0] = alternativePathDistance
                    vertex_data[adjV][1] = currentV

    return vertex_data

def Detect_Negative_cycle(Graph, startV):
    vertex_data = Bellman_Ford(Graph, startV)

    for i in range(len(Graph)-1):
        for currentV in Graph:
            for adjV in Graph[currentV]:
                edgeWeight = Graph[currentV][adjV]
                alternativePathDistance = vertex_data[currentV][0] + edgeWeight

                if alternativePathDistance < vertex_data[adjV][0] :
                    return True

    return False

def printallpaths(startV, vertex_data):
    for path in vertex_data:
        path_stack = []
        while(path != startV):
            path_stack.append(path)
            path = vertex_data[path][1]
        path_stack.append(path)
        print(path_stack.pop(), end='')
        while(len(path_stack)):
            print("-->" + path_stack.pop(), end='')
        print()





def main():
    # G = {'P': {'Q': 6, 'R': 2}, 'Q': {'P':6,'R':4}, 'R': {'P':2,'Q':4}}
    # print(Bellman_Ford(G, 'P'))
    # print(Detect_Negative_cycle(G, 'P'))

    GG = {'s': {'A':5, 'C':-2}, 'A': {'B':1}, 'B': {'D': -1, 't': 3}, 'C': {'A':2, 'B':4, 'D':4},
          'D': {'t': 1}, 't': {}}

    out_BF = Bellman_Ford(GG, 's')
    print(out_BF)
    printallpaths('s', out_BF)


if __name__ == '__main__':
    main()
