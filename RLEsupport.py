
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
