class Graph():
    def __init__(self, vertices):
        self.graph = {}
        self.V = vertices
 
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
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        recStack[v] = False
        return False
 
    def isCyclic(self):
        print(self.graph)
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in self.graph.keys():
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
 
if __name__ == '__main__':
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
 
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")