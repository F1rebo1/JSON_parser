from json_parser import lexer, parser

def test4():
    invalidPath = "./tests/step4/invalid.json"
    validPath = "./tests/step4/valid.json"
    validPath2 = "./tests/step4/valid2.json"

    pass1 = not lexer(invalidPath)
    pass2 = lexer(validPath)
    pass3 = lexer(validPath2)
    if pass1:
        print("> test1 invalid.json PASSED")
    else:
        print("> test1 invalid.json FAILED")
    
    print("-----------------------------")

    if pass2:
        print("> test2 valid.json PASSED")
    else:
        print("> test2 valid.json FAILED")
    
    print("-----------------------------")

    if pass3:
        print("> test3 valid.json PASSED")
    else:
        print("> test3 valid.json FAILED")

    if pass1 and pass2 and pass3:
        return 0
    else:
        return 1      

def test3():
    invalidPath = "./tests/step3/invalid.json"
    validPath = "./tests/step3/valid.json"

    pass1 = not lexer(invalidPath) or not parser(invalidPath)
    pass2 = lexer(validPath) and parser(validPath)
    if not pass1:
        print("> test1 invalid.json PASSED")
    else:
        print("> test1 invalid.json FAILED")
    
    print("-----------------------------")
    # print("#############################")

    # if pass2:
    #     print("> test2 valid.json PASSED")
    # else:
    #     print("> test2 valid.json FAILED")
    
    print("-----------------------------")
    return 0 if pass1 else 1
    # if pass1 and pass2:
    #     return 0
    # else:
    #     return 1      

def test2():
    # invalidPaths = ["./tests/step1/invalid.json", "./tests/step1/invalid.json"]
    # validPaths = ["./tests/step1/valid.json","./tests/step1/valid2.json"]

    invalidPath = "./tests/step2/invalid.json"
    invalidPath2 = "./tests/step2/invalid2.json"
    validPath = "./tests/step2/valid.json"
    validPath2 = "./tests/step2/valid2.json"

    pass1 = not lexer(invalidPath) or not parser(invalidPath)
    pass2 = not lexer(invalidPath2) or not parser(invalidPath2)
    pass3 = lexer(validPath) and parser(validPath)
    pass4 = lexer(validPath2) and parser(validPath2)

    invalidTests = [pass1,pass2]
    validTests = [pass3,pass4]

    res = True
    i = 1
    for test in invalidTests:
        if test:
            print(f"> test{i} invalid.json PASSED")
        else:
            print(f"> test{i} invalid.json FAILED")
        print("-----------------------------")
        i += 1
        res = res and test
    
    for test in validTests:
        if test:
            print(f"> test{i} valid.json PASSED")
        else:
            print(f"> test{i} valid.json FAILED")
        print("-----------------------------")
        i += 1
        res = res and test

    if res:
        return 0
    else:
        return 1   

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
    test = {test1:'t1', test2:'t2', test3:'t3', test4:'t4'}
    # testArr = {test3:'t3'}

    testNum = 1

    print("TESTING")
    for key, val in test.items():
        print()
        print("#############################")
        print(f"STEP {testNum}")
        print("-----------------------------")
        key()
        print("#############################")
        print()
        testNum += 1