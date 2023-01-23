
male=["harsha","munna"]

def check(inp1):
    if inp1 in male:
        print("male")
    elif inp1[len(inp1) - 1] == 'a' or inp1[len(inp1) - 1] == 'y' or inp1[len(inp1) - 1] == 'e' or \
            inp1[len(inp1) - 1] == 'i':
        print("feamle")
    else:
        print("male")


inp1 = input("enter a name")
check(inp1)
