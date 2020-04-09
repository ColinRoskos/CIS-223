# Task 5 | CIS 223-03 | Implement BFS
# Author: Colin Roskos
# Implement Breadth First Search (BFS)
#
# To represent a graph, we will use a dictionary and and array of adjacent nodes.
#
#        e.g. G=    (P)
#                   / \
#                 (Q)-(R)
#
#       is G={'P':['Q','R'], 'Q':['P','R'], 'R':['P','Q']}
#


def BFS(graph, vertex):
    frontier_queue = []
    visited_ordered = []
    discovered_set = set()

    frontier_queue.append(vertex)
    visited_ordered.append(vertex)
    discovered_set.add(vertex)

    while len(frontier_queue) > 0:
        search_vertex = frontier_queue.pop()
        for adjacent in graph[search_vertex]:
            if adjacent in discovered_set:
                continue
            frontier_queue.append(adjacent)
            visited_ordered.append(adjacent)
            discovered_set.add(adjacent)

    return visited_ordered

def DFS(graph, vertex):
    search_stack = []
    visited_ordered = []
    discovered_set = set()

    search_stack.insert(0, vertex)

    while len(search_stack) > 0:
        search_vertex = search_stack.pop()
        if search_vertex in discovered_set:
            continue
        discovered_set.add(search_vertex)
        visited_ordered.append(search_vertex)
        for c_vertex in graph[search_vertex]:
            if c_vertex in discovered_set:
                continue
            search_stack.insert(len(search_stack), c_vertex)

    return visited_ordered

def cycle_detect(graph, vertex=None, discovered_set=None, last_vertex=None):
    # recursive solution to cycle detect

    # if first cycle through
    if vertex is None:
        vertex = list(graph)[0]     # pick a starting vertex
    if discovered_set is None:
        discovered_set = set()      # init discovered to set()

    discovered_set.add(vertex)      # add current vertex to known verticies

    # step through each adjacent vertex
    for adjacent in graph[vertex]:
        # if the adjacent vertex has not already been discovered
        #     go down vertex until you find a dead end
        if adjacent not in discovered_set:
            if cycle_detect(graph, adjacent, discovered_set, vertex):
                # continue cycle return value
                return True
            continue
        # if the adjacent value has already been found and is that the previous value,
        #     then you have a cycle and should return True.
        if adjacent in discovered_set and adjacent != last_vertex:
            return True

    # if this is a dead end or all adjacent verticies lead to dead ends.
    return False


def main():

    main_graph = {'A':['C', 'B'], 'B':['A', 'D', 'E'], 'C':['A', 'F'], 'D':['B'], 'E':['B', 'F'], 'F':['C', 'E']}

    print(BFS(main_graph, 'A'))
    print(DFS(main_graph, 'A'))
    print(cycle_detect(main_graph))

    # removed vertex 'C'
    main_graph = {'A':['B'], 'B':['A', 'D', 'E'], 'D':['B'], 'E':['B', 'F'], 'F':['E']}

    print(cycle_detect(main_graph))




if __name__=='__main__':
    main()
