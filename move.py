import json

def resolveJson(path):
    file = open(path, "r")
    
    # fileJson = json.load(file)
    # field = fileJson["field"]
    # futures = fileJson["futures"]
    # type = fileJson["type"]
    # name = fileJson["name"]
    # time = fileJson["time"]
    return file


def output(path):
    file = open(path,"r+")
    print(file)
    i = 0
    for line in file.readline():
        # line = "".join(line.split())
        # print(line)
        i = i+1
    print(i)


path1 = "/Users/xingfeng/Python/Tools/7786.txt"
# output(path)
path2 = "/Users/xingfeng/Python/Tools/7786.txt"
file = open("./7786_pro.json","w+")


for line in open("./7786.json","r+"):
    line = "".join(line.split())
    file.write(line)
    print(line)