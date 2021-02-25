graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        n = queue.pop(0)
        print(n, end=" ")

        for neighbor in graph[n]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


bfs(visited, graph, "A")
