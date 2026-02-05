# Opgave 4 (Graph Transpose)
def graph_transpose(graph):
    transposed_graph = {} # empty dictionary
    
    # initialize empty graph with lists
    for node in graph:
        for edge in graph[node]:
            transposed_graph[edge] = []

    for node in graph:
        # print(f'Node: {node}')
        for edge in graph[node]:
            transposed_graph[edge].append(node)
            # print(f'Edge: {edge}')
    
    return transposed_graph