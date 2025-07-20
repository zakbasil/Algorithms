class Graph():
    def __init__(self, vertices):
        self.graph = {}
        self.V = vertices
 
    def addNewNode(self):
        self.V += 1

    
    def addEdge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v not in self.graph.keys():
            self.graph[v] = []

    
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True

        recStack[v] = False
        return False
 
    def isCyclic(self):
        print(self.graph)
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in self.graph.keys():
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False
 
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(2, 1)
    g.addEdge(1, 2)
    g.addEdge(4, 3)
    g.addEdge(3, 4)
 
    if g.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")