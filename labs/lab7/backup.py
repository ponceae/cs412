""" Lab 7: Graph Search Basics.

    Uses the whatever search first algorithm 
    to determine if a specified bus route
    is reachable, and if it is output a 
    valid route.

    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""
import queue


def wfs(adj, start, end):
""" The bag contains a tuple of the current node, 
    and the path used to reach said node. Once the 
    destination has been reached, it then returns 
    the used path.
"""
    marked = set()
    bag = queue.Queue()
    # put s in the bag
    bag.put((start, [start]))
    # while the bag is not empty
    while not bag.empty():
        # take v from the bag
        (v, path) = bag.get()
        # destination reached, return
        if v == end:
            return path
        # if v is not marked
        if v not in marked:
            # mark v
            marked.add(v)
            # for each edge vw
            for w in adj.get(v):
                # if w is not marked
                if w not in marked:
                    # put w in the bag
                    bag.put((w, path + [w]))
    # no route possible
    return []


def main():
    adj = {}
    n = int(input())
    for _ in range(n):
        s1, s2 = input().split()
        if s1 not in adj:
            adj[s1] = set()
        if s2 not in adj:
            adj[s2] = set()
        adj[s1].add(s2)
        adj[s2].add(s1)
    query = input().split()
    path = wfs(adj, query[0], query[1])
    # output formatting
    if not path:
        print('no route possible')
    else:
        print(*path)


if __name__ == "__main__":
    main()
