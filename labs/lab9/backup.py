""" Lab 10: Shortest Paths
    
    This program implements Djikstra's algorithm
    for finding the shortest path in a weighted,
    directed graph given input of n vertices,
    m edges, and determines if a query q is 
    possible or not.

    Name: 
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""
from queue import PriorityQueue


def initSSSP(start, num_v):
    dist = {}  
    pred = {}
    dist[start] = 0     # dist from start to itself is 0
    pred[start] = None  # start pred is initially None
    for v in range(num_v):
        # Exclude the start node.
        if v != start:
            dist[v] = float("inf")
            pred[v] = None
    return dist, pred


def relax_edge(u, v, dist, pred, w):
    dist[v] = dist[u] + w   # Formula for relaxing an edge.
    pred[v] = u


def djikstras(adj, start, end, num_v):
    pq = PriorityQueue()
    # Initialize dist and pred
    dist, pred = initSSSP(start, num_v)
    if start == end:
        return 0
    for v in range(num_v):
        pq.put((v, dist[v]))
    while not pq.empty():
        # u = ExtractMin()
        u = pq.get()[0]
        # Path is complete, terminate
        if u == end:
            return dist[end]
        # Guarantees that u is a reachable vertex.
        if adj.get(u, None) is not None:
            # Iterate through the neighbors of u.
            for v, w in adj[u]:
                # Guarantees that v is a reachable vertex.
                if dist.get(v, None) is not None: 
                    # If u->v is tense:
                    if dist[u] + w <= dist[v]:
                        # Relax(u->v)
                        relax_edge(u, v, dist, pred, w)
                        # DecreaseKey(v, dist(v))
                        pq.put((v, dist[v]))
    # Default return
    return None


def main():
    adj = {}
    # num vertices, num edges, and num queries
    num_v, num_m, num_q = map(int, input().split())
    for _ in range(num_m):
        # vertices u->v with a weight of w
        u, v, w = map(int, input().split())
        # Creates a directed graph where u->(v,w).
        if u not in adj:
            adj[u] = []
        adj[u].append((v, w))
    for _ in range(num_q):
        # Extract the query and pass it to Djikstra's algorithm.
        start, end = map(int, input().split())
        dist = djikstras(adj, start, end, num_v)
        # Infinite distance means that t is not reachable from s.
        if dist != float("inf") and dist is not None:
            print(dist)
        else:
            print("Impossible")


if __name__ == "__main__":
    main()
