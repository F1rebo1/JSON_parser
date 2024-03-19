# class jsonType:
#     def __init__(self):
#         self.objType = 

# class jsonObj:
#     def __init__(self, jsonType):

def parser(data):
    with open(data,"r") as file:
        json = []
        for line in file:
            # print(line)
            line = line.strip()
            # line = line.replace('{','')
            # line = line.replace('}','')
            line = line.split(',')
            # line = line.replace(': ',', ')
            # line = line.replace('{','')
            # line = line.replace('}','')
            # line = line.split(', ')
            # print(line)
            for val in line:
                json.append(val)
        
        file.close()
        # print(json)
    
    res = True
    for val in json:
        val = val.split(': ')
        # print(val)
        if(len(val) > 1):
            # print(val[1])
            if(val[1] == 'True' or val[1] == 'False'):
                res = False
                # print('Invalid bool expr: ' + str(val[1]) + '. Should be ' + str(val[1].lower()))
        

    print("===========================")
    return res

def lexer(data):
    with open(data,"r") as file:
        json = ""
        for lines in file:
            json += lines.strip("\n")
        
        file.close()
        
        if len(json) < 2:
            return False
        
        if json[0] == '{' and json[-1] == '}':
            return True
        else:
            return False
        
def main():
    from testing import runTests
    runTests()
    # lexer(data)

if __name__ == "__main__":
    main()