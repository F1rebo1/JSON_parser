def parser(data):
    with open(data,"r") as file:
        print("Henlo")

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