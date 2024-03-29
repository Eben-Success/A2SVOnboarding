# --------------------------------------
# Function to convert Adjacency List to Adjacency Matrix
def adjacency_list_to_matrix(adj_list):

# Write your code here to convert the adjacency list to an adjacency matrix
    adj_matrix = [[0 for i in range(len(adj_list))] for j in range(len(adj_list))]
    
    for key, val in adj_list.items():
        for i in val:
            adj_matrix[key][i] = 1

    return adj_matrix

# Test case
adj_list_sample = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

result_matrix = adjacency_list_to_matrix(adj_list_sample)
expected_result = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

# Print the result for verification
print("Result:", result_matrix)
if result_matrix == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")
# --------------------------------------


# --------------------------------------
# Function to convert Adjacency Matrix to Adjacency List
def adjacency_matrix_to_adjacency_list(adj_matrix):
    adj_list = {}

    # Write your code here to convert the adjacency matrix to an adjacency list
    # Your code goes here
    
    for r in range(len(adj_matrix)):
        for c in range(len(adj_matrix[r])):
            if adj_matrix[r][c] == 1:
                if r not in adj_list:
                    adj_list[r] = [c]
                else:
                    adj_list[r].append(c)

    return adj_list  # Return the adjacency list

# Test case
adj_matrix_sample = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

# --- Student Section to Write Code ---
# Write your code for the conversion here
result_adj_list = adjacency_matrix_to_adjacency_list(adj_matrix_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")
# --------------------------------------


from collections import defaultdict

# --------------------------------------
# Function to convert Edge List to Adjacency List
def edge_list_to_adjacency_list(edge_list):

	# Write your code here to convert the edge list to an adjacency list.
   
    adj_list = defaultdict(list)
    for i in edge_list:
        adj_list[i[0]].append(i[1])
        
    return adj_list

# Test case
edge_list_sample = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

# --- Student Section to Write Code ---
# Write your code for the conversion here
result_adj_list = edge_list_to_adjacency_list(edge_list_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")
# --------------------------------------


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
    
    
    
    
