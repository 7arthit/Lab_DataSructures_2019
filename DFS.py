def DFS(graph, start, path =  None):
    if path is None:
        path = set()
    path.add(start)
    print(start[::-1])

    for move in graph[start] - path:
        DFS(graph, move, path)
    return path
graph = {'1': set(['9', '5', '2']),
         '9': set(['6', ]),
         '6': set(['7', '5', '9']),
         '7': set(['8']),
         '5': set(['2', '1','6']),
         '2': set(['1', '5', '3']),
         '3': set(['2', '4']),}
DFS(graph ,'1')