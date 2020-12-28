import re
newlines = []
with open("./test1.txt", "r+") as file:
    content = file.readlines()
    for line in content:
        matches = re.match("from cppyy.gbl import (.*)", line)
        if matches:
            print("Matches are:")
            print(matches)
            print(type(matches[1]))

            print(matches[1])
            update = "{} = TopologicCore.{}".format(matches[1], matches[1])
            print(update)
            newlines.append(update)
    newcontent = "\r\n".join(newlines)
    print(newcontent)
    with open("./test2.txt", "w+") as file2:
        file2.write(newcontent)

