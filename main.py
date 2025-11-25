from collections import deque
from heapq import heappush, heappop

def shortest_shortest_path(graph, source):
    dist = {}
    for v in graph:
        dist[v] = (float('inf'), float('inf'))
    dist[source] = (0, 0)
    heap = []
    heappush(heap, (0, 0, source))
    while heap:
        w_u, e_u, u = heappop(heap)
        if (w_u, e_u) != dist[u]:
            continue
        for v, w_uv in graph[u]:
            new_w = w_u + w_uv
            new_e = e_u + 1
            old_w, old_e = dist[v]
            if (new_w < old_w) or (new_w == old_w and new_e < old_e):
                dist[v] = (new_w, new_e)
                heappush(heap, (new_w, new_e, v))
    return dist

def bfs_path(graph, source):
    parents = {}
    visited = set([source])
    q = deque([source])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parents[v] = u
                q.append(v)
    return parents

def get_sample_graph():
    return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}}

def get_path(parents, destination):
    path_nodes = []
    node = destination
    while node in parents:
        parent = parents[node]
        path_nodes.append(parent)
        node = parent
    path_nodes.reverse()
    return ''.join(path_nodes)
