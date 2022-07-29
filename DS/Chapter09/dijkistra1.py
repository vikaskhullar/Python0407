# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:23:00 2022

@author: vikas
"""

# Python program for Dijkstra's single

class Graph():
    def __init__(self):
        
        #self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.graph=[]
        
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
    
    def minDistance(self, dist, sptSet):
        min = 1e7
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    def dijkstra(self, src, vertices):
        for row in range(vertices):
            c=[]
            for column in range(vertices):
                c.append(0)
            self.graph.append(c)

        self.V = vertices
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)



n=5

g = Graph()

g.graph=[
        [0,3,0,5,0],
        [3,0,7,0,2],
        [0,7,0,4,1],
        [5,0,4,0,0],
        [0,2,1,0,0] 
        ]


'''
g.graph = 
        [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]
'''



g.dijkstra(0, 5)

# This code is contributed by Divyanshu Mehta
