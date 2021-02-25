graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            return path
        for neighbor in graph[source]:
            path = dfs(graph, neighbor, path)
    return path


path = dfs(graph, "A")

print(" ".join(path))
