"""Lab 13: NP-Completeness Part D

    Name:
        Adrien Ponce
    Honor Code:
        This code complies with the JMU Honor Code.
"""


def verify_ind_set(adj, query):
    for u in query:
        for v in query:
            if adj[u] is not None:
                if u != v and v in adj[u]:
                    return False
    return True


def main():
    adj = {}
    n = int(input())
    for i in range(n):
        adj[i] = None
        edge_list = list(map(int, input().split()))
        edge_list.pop(0)
        if len(edge_list) != 0:
            adj[i] = set(edge_list)
    query = set(map(int, input().split()))
    print(verify_ind_set(adj, query))


if __name__ == "__main__":
    main()
