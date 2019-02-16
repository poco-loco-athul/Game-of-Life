
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
                #empty line
                if n.isnumeric():
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
    return matrix
            
    
