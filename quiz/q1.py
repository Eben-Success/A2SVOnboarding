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
