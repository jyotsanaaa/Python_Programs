#Sum of two matrices

mat1 = [[2,5],
        [4,3],
        [6,1]]

mat2 = [[7,9],
        [8,6],
        [4,3]]

result = [[0,0],
          [0,0],
          [0,0]]

#iteration through rows
for i in range(len(mat1)):
    #iteration through column
    for j in range(len(mat1[0])):
        result[i][j] = mat1[i][j] + mat2[i][j]
        
for r in result:
    print(r)