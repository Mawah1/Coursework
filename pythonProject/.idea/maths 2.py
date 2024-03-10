# import numpy as np
# E = np.array([[0,1,1,0,0,1,0,1],[1,0,0,0,1,0,1,0],[1,0,0,1,0,1,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,1,0],[1,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1],[1,0,0,0,0,0,1,0]])
# A = np.array([[0,1,1,0,0,1,0,1],[1,0,0,0,1,0,1,0],[1,0,0,1,0,1,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,1,0],[1,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1],[1,0,0,0,0,0,1,0]])
# C = np.array([[0,1,1,0,0,1,0,1],[1,0,0,0,1,0,1,0],[1,0,0,1,0,1,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,1,0],[1,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1],[1,0,0,0,0,0,1,0]])
# walk_of_3 = E * A * C
# print(walk_of_3)

import numpy as np

# Example adjacency matrix
adjacency_matrix = np.array([[0,1,1,0,0,1,0,1],
                             [1,0,0,0,1,0,1,0],
                             [1,0,0,1,0,1,0,0],
                             [0,0,1,0,0,0,0,0],
                             [0,1,0,0,0,0,1,0],
                             [1,0,1,0,0,0,0,0],
                             [0,1,0,0,1,0,0,1],
                             [1,0,0,0,0,0,1,0]])

# Cubing the matrix
cubed_matrix = adjacency_matrix @ adjacency_matrix @ adjacency_matrix

# Display the result
print("Cubed Adjacency Matrix:\n", cubed_matrix)



#vector_b = np.array([26,7,2,23])
# x = inverse_E @ vector_b
# answer1 = x[0][0]+x[0][1] + x[0][2] + x[0][3]
# answer2 = x[1][0]+x[1][1] + x[1][2] + x[1][3]
# answer3 = x[2][0]+x[2][1] + x[2][2] + x[2][3]
# answer4 = x[3][0]+x[3][1] + x[3][2] + x[3][3]
# print(answer1)
# print(answer2)
# print(answer3)
# print(answer4)
#print(x)
