from collections import defaultdict
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n <= 2:
        return [i for i in range(n)]

    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    leaves = [node for node in graph.keys() if len(graph[node]) == 1]

    while n > 2:
        n -= len(leaves)
        new_leaves = set()
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.add(neighbor)

        leaves = new_leaves

    return leaves


n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(findMinHeightTrees(n, edges))