from collections import defaultdict

def edge_list_to_adjacency_list(edge_list):

	# Write your code here to convert the edge list to an adjacency list.
   
    adj_list = defaultdict(list)
    for i in edge_list:
        adj_list[i[0]].append(i[1])
        
    return adj_list

def edge_list_to_adj_matrix(edge_list):
    
    # convert edge_list to adj_list
    adj_list = edge_list_to_adjacency_list(edge_list)
    
    # convert adj_list to adj_matrix
    adj_matrix = [[0 for _ in range(len(adj_list))] for _ in range(len(adj_list))]
    
    for key, val in adj_list.items():
        for i in val:
            adj_matrix[key][i] = 1
    
    return adj_matrix
    

edge_list = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
print(edge_list_to_adj_matrix(edge_list))
    
    
    
    