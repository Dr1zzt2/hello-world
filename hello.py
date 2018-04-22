import sys
def namecheck():
    if len(sys.argv) < 2:
        name = "World"
    else:
        name = str(sys.argv[1])
    return(name)
print(f"Hello {namecheck()}!")