visited = []
N = int(input())
edges = {}

def detectLoop(node):
    print(node)
    if not visited[node]:
        visited[node] = True
        nextItems = edges[node]
        for i in nextItems:
            if detectLoop(i) == True:
                return(True)
        return(False)
    else:
        return(True)


for i in range(N):
    ListOfNodes = []
    a, b = list(map(int, input().rstrip().split(' ')))
    ListOfNodes.append(a)
    ListOfNodes.append(b)

    if a in edges.keys():
        edges[a].append(b)
    else:
        edges[a] = [b]

ListOfNodes = list(set(ListOfNodes))
numberOfNodes = len(ListOfNodes) 
visited = [False]*numberOfNodes
print(visited, numberOfNodes, edges)
detectLoop(list(edges.keys())[0])




    # else:
    #     print('Loop exist')