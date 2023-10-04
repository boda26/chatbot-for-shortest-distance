def getGraph(graph):
    paths = graph['graph'].split(',')
    nodes = set()
    adjList = {}
    dists = {}

    for path in paths:
        node1, node2 = path.split('->')
        if node1 in adjList:
            adjList[node1].append(node2)
        else:
            adjList[node1] = [node2]
        nodes.add(node1)
        nodes.add(node2)
        dists[(node1, node2)] = 1
    nodes = list(nodes)
    for n in nodes:
        if n not in adjList:
            adjList[n] = []

    for a in nodes:
        for b in nodes:
            if a == b:
                dists[(a,b)] = 0
            elif (a,b) not in dists:
                dists[(a,b)] = bfs(adjList, a, b)
            elif (a,b) in dists:
                dists[(a,b)] = min(dists[(a,b)], bfs(adjList, a, b))
    print(dists)

def bfs(adjList, src, dst):
    q = [src]
    level = {src: 0}
    while q:
        cur = q.pop(0)
        for n in adjList[cur]:
            if n not in level:
                q.append(n)
                level[n] = level[cur] + 1
    return level[dst] if dst in level else -1


    
graph = {"graph": "New York->New Jersey,New Jersey->Boston,Boston->Philadelphia,New York->Washington,New York->Miami,New Jersey->Houston,Boston->Houston,Miami->Austin,Los Angeles->New Jersey,Los Angeles->Philadelphia,San Francisco->Las Vegas,Las Vegas->Washington,Houston->Las Vegas,Chicago->New Jersey,Los Angeles->Chicago"}
getGraph(graph)
