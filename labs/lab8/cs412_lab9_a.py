""" Lab 9: Minimum Spanning Trees

    This program implements Boruvka's MST algorithm to find
    the minimum cost of building railroad tracks for a given 
    graph. 

    Name:
        Adrien Ponce
    Honor Code and Acknowledgements:
        This code complies with the JMU Honor Code. This algorithm
        also uses the count_and_label and dfs_label() algorithms
        written by Professor Bowers and Professor Molloy with
        slight modifications.
"""
import math


def dfs_label(graph, v, labels, currentLabel):
    bag = [v]
    while bag: # while bag is not empty
        u = bag.pop()
        if labels[u] == -1:
            labels[u] = currentLabel
            for w in graph[u]:
                bag.append(w)


def count_and_label(graph):
    labels = {v: -1 for v in graph.keys()} # Initially all labels are 0
    count = -1
    for v in graph.keys(): # for each vertex
        if labels[v] == -1: # if v is not visited
            count += 1
            dfs_label(graph, v, labels, count)
    return count+1, labels


def boruvka(adj, weights):
    # F = (V, None)
    forest = {v: set() for v in adj.keys()}
    # componentCount = CountAndLabel(F)
    comp_count, labels = count_and_label(forest)
    # while componentCount > 1:
    while comp_count > 1:
        # AddAllSafeEdges(E, F, componentCount)
        add_all_safe_edges(weights, forest, labels, comp_count)
        # componentCount = CountAndLabel(F)
        comp_count, labels = count_and_label(forest)
    return forest


def add_all_safe_edges(weights, forest, comp, count):
    # safe = [None] * count
    safe = [None] * count
    # for u, v in E:
    for (u, v), w in weights.items():
        # if comp(u) != comp(v):
        if comp[u] != comp[v]:
            w = weights[(u, v)]
            # if safe[comp[u]] == None or w(uv) < w(safe[comp(u)])
            if safe[comp[u]] is None or w < weights[(safe[comp[u]][0], safe[comp[u]][1])]:
                # safe[comp[u]] = uv
                safe[comp[u]] = (u, v)
            # if safe[comp[v]] == None or w(uv) < w(safe[comp(v)]):
            if safe[comp[v]] is None or w < weights[(safe[comp[v]][0], safe[comp[v]][1])]:
                    # safe[comp[v]] = uv
                    safe[comp[v]] = (u, v)
    # for e in safe:
    for e in safe:
        # add e to F
        if e is not None:
            u, v = e
            forest[u].add(v)
            forest[v].add(u)


def compute_distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    adj = {}
    weights = {}
    n = int(input())
    for _ in range(n):
        x, y, = map(float, input().split())
        # Coordinate point has not yet been added to the adjacency list.
        if (x, y) not in adj:
            adj[(x, y)] = set()
        # Iterate through all of the coordinate points.
        for (u, v) in adj.keys():
            # Add an edge between the two coordinates.
            if (u, v) != (x, y):
                adj[(x, y)].add((u, v))
                adj[(u, v)].add((x, y))
                # Store the distance between those two points.
                weights[((x, y), (u, v))] = compute_distance(x, y, u, v)
                weights[((u, v), (x, y))] = compute_distance(u, v, x, y)
    MST = boruvka(adj, weights)
    cost = 0.0
    for (x1, y1), vw in MST.items():
        for (x2, y2) in vw:
            if (x2, y2) >= (x1, y1):
                w = weights[((x1, y1), (x2, y2))]
                cost += w
    print("${:.1f}M".format(cost))


if __name__ == "__main__":
    main()
