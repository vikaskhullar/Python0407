graph = dict() 
graph['A'] = ['B', 'C'] 
graph['B'] = ['E','C', 'A'] 
graph['C'] = ['A', 'B', 'E','F'] 
graph['E'] = ['B', 'C'] 
graph['F'] = ['C']

graph
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)  

cols
'''
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)] 
'''

adjacency_matrix=[]

for y in range(cols):
    ls=[]
    for x in range(rows):
        ls.append(0)
    adjacency_matrix.append(ls)
adjacency_matrix



import numpy as np
adjacency_matrix = np.zeros((5,5)).astype(int).tolist()


edges_list = [] 


for key in matrix_elements: 
    for neighbor in graph[key]: 
        edges_list.append((key,neighbor)) 

print(edges_list)


for edge in edges_list: 
        index_of_first_vertex = matrix_elements.index(edge[0]) 
        index_of_second_vertex = matrix_elements.index(edge[1]) 
        adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1 


print(adjacency_matrix)
