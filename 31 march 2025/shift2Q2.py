# Problem Recap:
# We have N towers in a tree (connected and acyclic with N-1 edges).

# Each tower i has:

# A[i]: crystals needed to restore it.

# B[i]: power spread that reduces the A value of directly connected neighbors when tower i is restored.

# Given K crystals, we must maximize the number of towers restored.

from collections import defaultdict, deque

def restore_towers(n, k, A, B, edges):
    graph = defaultdict(list)
    
    # Build the tree
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    restored = [False] * n
    remaining = k
    result = 0

    def dfs_restore(node, parent):
        nonlocal remaining, result
        if restored[node] or A[node] > remaining:
            return
        
        # Use crystals to restore current tower
        remaining -= A[node]
        restored[node] = True
        result += 1

        # Spread the B[i] effect
        for neighbor in graph[node]:
            if not restored[neighbor]:
                A[neighbor] = max(0, A[neighbor] - B[node])

        # Continue DFS
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs_restore(neighbor, node)

    # Try to restore towers in increasing order of A[i]
    while True:
        min_cost = float('inf')
        start = -1
        for i in range(n):
            if not restored[i] and A[i] < min_cost and A[i] <= remaining:
                min_cost = A[i]
                start = i

        if start == -1:
            break  # No more towers can be restored

        dfs_restore(start, -1)

    return result


# Sample input
n = 4
k = 9
A = [5, 10, 3, 4]
B = [1, 5, 2, 2]
edges = [(0,1), (1,2), (2,3)]

print("Maximum towers restored:", restore_towers(n, k, A, B, edges))


