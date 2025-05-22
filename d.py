import heapq
graph = [
    [0, 1, 4, 0],  # Node 0
    [1, 0, 2, 5],  # Node 1
    [4, 2, 0, 1],  # Node 2
    [0, 5, 1, 0]   # Node 3
]

start = 0
end = 3

def diksh(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    heap = [(0,start)]

    while heap:
        curr_dis, u = heapq.heappop(heap)
        if u == end :
            return curr_dis
        
        if visited[u]:
            continue

        visited[u] = True

        for v in range(n):
            weight = graph[u][v]
            if weight > 0 and not visited[v]:
                new_dis = curr_dis + weight
                if new_dis < dist[v]:
                    dist[v] = new_dis
                    heapq.heappush(heap, (new_dis, v))
    return -1                


print(diksh(graph, start , end))