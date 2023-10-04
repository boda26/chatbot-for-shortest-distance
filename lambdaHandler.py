import boto3

def lambda_handler(event, context):
    graph = event
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
    #print(dists)
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    graphTable = dynamodb.Table('graphTable')
    try:
        with graphTable.batch_writer() as batch:
            for (src, dst), dist in dists.items():
                path = src + "-" + dst
                batch.put_item(Item={'path': path, 'source': src, 'destination': dst, 'distance': dist})
        return {
            'statusCode': 200,
            'message': 'Successfully added to database'
        }    
    except Exception as e:
        return {
            'statusCode': 500,
            'message': 'Error in adding to database'
        }


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
