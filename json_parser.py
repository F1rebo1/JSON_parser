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

def test1():
    invalidPath = "./tests/step1/invalid.json"
    validPath = "./tests/step1/valid.json"

    pass1 = not lexer(invalidPath)
    pass2 = lexer(validPath)
    if pass1:
        print("> test1 invalid.json PASSED")
    else:
        print("> test1 invalid.json FAILED")
    
    print("-----------------------------")
    # print("#############################")

    if pass2:
        print("> test2 valid.json PASSED")
    else:
        print("> test2 valid.json FAILED")
    
    print("-----------------------------")
    if pass1 and pass2:
        return 0
    else:
        return 1        

def runTests():
    print("TESTING")
    print()
    print("#############################")
    print("STEP 1")
    print("-----------------------------")
    print(test1())
    print("#############################")

def main():
    runTests()
    # lexer(data)

if __name__ == "__main__":
    main()