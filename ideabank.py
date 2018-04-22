import sys
i = 0
d = 0
path = '/users/dr1zzt/documents/python/ideabank.txt'
if len(sys.argv) == 1:
    ideabank_file = open(path,"a")
    ideabank_file.write((input("New Idea: ")))
    ideabank_file.write("\n")
    ideabank_file.close()
elif len(sys.argv) == 2 and str(sys.argv[1]) == "--list":
    ideabank_file = (open(path,"r"))
    for line in ideabank_file:
        i = i + 1
        print(f"{i}. {line}")
    ideabank_file.close()
elif len(sys.argv) == 3 and str(sys.argv[1]) == "--delete":
    ideabank_file = open(path,"r+")
    d = int(sys.argv[2])
    r = ideabank_file.readlines()
    ideabank_file.seek(0)
    for line in r:
        i = i + 1
        if i != d:
            ideabank_file.write(line)
    ideabank_file.truncate()
    ideabank_file.close()