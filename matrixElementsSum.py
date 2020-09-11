def matrixElementsSum(matrix):
    l = []

    for i in matrix:
        for x in range(len(matrix[0])):
            if matrix.index(i) != 0:
                if i[x] != 0:
                    if i.count(i[x]) == 1:
                        z = matrix.index(i) - 1
                        if matrix[z][i.index(i[x])] != 0:
                            l.append(i[x])
                    
                    else:
                        for b in range(i.count(i[x])):
                            print(i.index(i[x]))

print(matrixElementsSum([[0,1,1,2], 
 [0,5,0,0], 
 [2,0,3,3]]))