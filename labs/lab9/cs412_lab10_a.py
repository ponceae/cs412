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
    pred, dist = {}, {}
    for v in range(num_v):
        dist[v] = float("inf")
        pred[v] = None
    # dist from start to itself is 0
    dist[start] = 0     
    return pred, dist


def djikstras(adj, start, end, num_v):
    pq = PriorityQueue()
    # init pred and dist
    pred, dist = initSSSP(start, num_v)
    for v in range(num_v):
        pq.put((v, dist[v]))
    while not pq.empty():
        # u = ExtractMin()
        u = pq.get()
        # end node reached
        if u[0] == end:
            if dist[end] != float("inf"):
                print(dist[end])
                return 0
        for u in adj:
            v = adj[u][0][0]
            w = adj[u][0][1]
            # if u->v is tense:
            if dist[u] + w < dist[v]:
                # Relax(u->v)
                dist[v] = dist[u] + w
                pred[v] = u
                # DecreaseKey(v,dist(v)
                pq.put((v, dist[v]))
    print("Impossible")
    return 0


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
        djikstras(adj, start, end, num_v)


if __name__ == "__main__":
    main()
