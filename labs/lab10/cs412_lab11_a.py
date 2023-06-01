""" Lab 11: Capacity Improvements

    This program identifies bottlenecks in a graph G and 
    computes the max flow of G and identifies the edges that
    cross the min cut using Ford-Fulkerson's algorithm.
        
    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code
"""
import queue


def ford_fulkerson(adj, num_v, source, sink):
    # Create a copy of original graph based on capacity.
    residual = copy_graph(adj, num_v)
    # Find one valid augmenting path before looping.
    path, pc_dict = bfs(residual, source, sink)
    while path:
        min_flow = get_min_flow(pc_dict, source, residual)
        residual = build_residual(min_flow, adj, pc_dict, num_v, source)
        return


def find_path_parents(path, marked):
    pc_dict = {0: None}
    for child in marked:
        if child in path:
            pc_dict[child] = marked[child]
    return pc_dict


def get_min_flow(pc_dict, source, residual):
    min_flow = float('inf')
    # Path nodes
    for v in pc_dict.keys():
        # Source parent will be None, ignore
        if v != source:      
            parent = pc_dict[v]
            # p->v max flow
            flow = int(residual[parent][v][0])
            # Extract the minimum valued flow
            min_flow = min(min_flow, flow)
    return min_flow


def build_residual(min_flow, adj, pc_dict, num_v, source):
    print(pc_dict)
    residual = {}
    # Create an empty dictionary for each vertice in adj.
    for v in range(num_v):
        residual[v] = {}
        # Iterate through all of the neighbors
        for u in adj[v]:
            # Remaining flow and capacity.
            edge = adj[v][u]
            # Gather parent of u from BFS traversal
            parent = pc_dict.get(u, None)
            # Verify that v is part of the path
            if v in pc_dict and v == parent:
                # Update the flow of the edge 
                adj[v][u][0] += min_flow
                # Residual graph takes adj max capacity - min_flow
                residual[v][u] = [edge[1] - min_flow]
            else:
                # Add edge normally, no flow detected. (i.e., not in path)
                residual[v][u] = [edge[1]]
            # Create a reverse edge since capacity is still left
            if u not in residual:
                residual.update({u: [987397]})
    print(residual)    


def copy_graph(adj, num_v):
    residual = {}
    # Create an empty dictionary for each vertice in adj.
    for v in range(num_v):
        residual[v] = {}
        # Iterate through all of the neighbors
        for u in adj[v]:
            # Remaining flow and capacity.
            edge = adj[v][u]
            # Only copy over the remaining capacity
            residual[v][u] = [edge[1]]
    return residual
    

def bfs(adj, source, sink):
    # Queue is used for BFS
    bag = queue.Queue()
    # Keeps track of visited nodes and the node's parents
    marked = {source: None}
    bag.put(source)
    while not bag.empty():
        v = bag.get()
        # Sink reached, build the path
        if v == sink:
            path = []
            while v:
                path.append(v)
                v = marked[v]
            pc_dict = find_path_parents(path, marked)
            return path[::-1], pc_dict
        # Iterate through V's edges
        for u in adj[v]:
            # Edge has not yet been explored
            if u not in marked:
                marked[u] = v
                bag.put(u)
    # No path found
    return None, None
    
    
def main():
    adj = {}
    # Number of vertices and edges.
    num_v, num_e = map(int, input().split())
    # Source is always 0, target is always V-1
    source, sink = 0, num_v - 1
    for i in range(num_v):
        adj[i] = {}
    for _ in range(num_e):
        # Vertice u->v with a max capacity of cap.
        u, v, cap = map(int, input().split())
        # Create a directed graph u->v with empty capacity.
        adj[u][v] = [0, cap]
    ford_fulkerson(adj, num_v, source, sink)


if __name__ == "__main__":
    main()
