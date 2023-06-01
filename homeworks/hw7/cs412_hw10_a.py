""" Coding Homework 10: Arbitrages
    
    This code detects currency arbitrages in 
    a graph given an input file of a list
    of currency exchanges and their
    corresponding rates.
        
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
    # Distance from the start to itself is 0
    dist[start] = 0     
    return pred, dist


def bellman_ford(adj, num_v):
    cycle = []
    # Populate the cycle with all currency keys.
    for key in adj.keys():
        cycle.append(key)
    # Create pred and dist structures for EACH node (currency).
    for node in adj:
        pred, dist = initSSSP(node, adj)
        # Iterate through V-1 edges
        for _ in range(num_v - 1):
            for u in adj:
                v = adj[u][0][0]
                w = adj[u][0][1]
                # If u->v is tense:
                if dist[u] + w < dist[v]:
                    # Relax (u->v)
                    dist[v] = dist[u] + w
                    pred[v] = u
    # Edges can still be relaxed after V-1 iterations.
    for u in adj:
        v = adj[u][0][0]
        w = adj[u][0][1]
        # If u->v is tense:
        if dist[u] + w < dist[v]:
            # Print the negative cycle based on the current currency.
            print("Arbitrage Detected")
            # Append the start currency to the end of the negative cycle.
            cycle.append(cycle[0])
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
    # Stores the final exchange rate.
    rate = 1
    # Number of exchange rates
    n_rates = int(input())      
    for _ in range(n_rates):
        # The start and end currencies with its exchange rate.
        c_in, c_out, r = input().split()
        r = float(r)
        rate *= r
        if c_in not in adj:
            adj[c_in] = []
        # Convert the rate to the negation of its log.
        adj[c_in].append((c_out, -log(r)))
    cycle = bellman_ford(adj, n_rates)
    # Unwrap negative cycle list if valid
    print_cycle(cycle, rate) if cycle else None
        

if __name__ == "__main__":
    main()
