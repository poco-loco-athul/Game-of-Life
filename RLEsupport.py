def RLE_to_string(value):
    "Decodes RLE into readable string format"
    number = []
    output = ""
    
    for i in value:
        n = "" 
        if i.isnumeric():
            number.append(i)
        else:
            n = "".join(number)
            if n == "":
                n = "1" 
            if i == "b":
                output += "False "*int(n)
            if i == "o":
                output += "True "*int(n)
            if i == "$":
                if n.isnumeric():
                    #empty line
                    for j in range(int(n)-1):
                        output += ";False "
                output += ";"
            number = []
    return output.strip()


def string_to_matrix(string):
    "Converts string into matrix with boolean values"
    boolDict = { 'True' : True, 'False' : False }
    strSplit = string.split(' ;')
    matrix = []
    
    for item in strSplit:
        submatrix = []
        for i in item.split(' '):
            submatrix.append(boolDict[i])
        matrix.append(submatrix)
    return matrix


def expand_matrix(matrix,m=3, n=3):
    "RLE files are designed to work in infinite grid. To make compatible we expands the matrix"
    # adding m cols and n rows on both sides
    row = len(matrix)
    
    for i in range(m):
        for i in range(row):
            matrix[i].insert(0, False)
    for j in range(n):
        matrix.insert(0,[False])
        matrix.append([False])
    return matrix
            
    
def fill_matrix(mat,x,y,m=3,n=3):
    "Dead cells at the end of a pattern line do not need to be encoded, so it has to be filled"
    row = len(mat)
    
    for i in range(row):
        while True:
            col = len(mat[i])
            if col == x +2*m:
                break
            mat[i].append(False)
    return mat


def decode(RLE, x, y, m=3, n=3):
    "Decodes RLE value into matrix"
    strg = RLE_to_string(RLE)
    mtrx = string_to_matrix(strg)
    e_mtrx = expand_matrix(mtrx, m=m, n=n)
    f_mtrx = fill_matrix(e_mtrx, x=x, y=y, m=m, n=n)
    return f_mtrx
