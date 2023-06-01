""" Coding Homework 10: Arbitrages
    
    This code detects currency arbitrages in 
    a graph of currencies.
        
    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""
from math import log


def initSSSP(start, adj):
    pred, dist = {}, {}
    for v in adj:
        dist[v] = float("inf")
        pred[v] = None
    # dist from start to itself is 0
    dist[start] = 0     
    return pred, dist


def bellman_ford(adj, num_v):
    cycle = []
    # Populate cycle for output
    for key in adj.keys():
        cycle.append(key)
    # Create pred and dist for EACH node
    for node in adj:
        pred, dist = initSSSP(node, adj)
        # Iterate through v - 1 edges
        for _ in range(num_v - 1):
            for u in adj:
                v = adj[u][0][0]
                w = adj[u][0][1]
                # If u->v is tense:
                if dist[u] + w < dist[v]:
                    # Relax(u->v)
                    dist[v] = dist[u] + w
                    pred[v] = u
    # Edges can still be relaxed after v - 1 iterations.
    for u in adj:
        v = adj[u][0][0]
        w = adj[u][0][1]
        # If u->v is tense:
        if dist[u] + w < dist[v]:
            # Print negative cycle based on current currency
            print("Arbitrage Detected")
            # Append end of cycle and return
            start = cycle[0]
            cycle.append(start)
            return cycle
    print("No Arbitrage Detected")
    return None

def print_cycle(cycle, rate):
    for i in range(len(cycle)):
            if i == len(cycle) - 1:
                print(cycle[i], end = "\n")
            else:
                print(cycle[i], end = " => ")
    print("{:.5f} factor increase".format(rate))
    

def main():
    adj = {}
    # stores final exchange rate
    rate = 1
    # num exchange rates
    n_rates = int(input())
    for _ in range(n_rates):
        # start & end currency, exchange rate
        c_in, c_out, r = map(str, input().split())
        r = float(r)
        rate *= r
        if c_in not in adj:
            adj[c_in] = []
        # negate the log of r
        adj[c_in].append((c_out, -log(r)))
    cycle = bellman_ford(adj, n_rates*2)
    # Unwrap negative cycle list
    if cycle:
        print_cycle(cycle, rate)
        


if __name__ == "__main__":
    main()
