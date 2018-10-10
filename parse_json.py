import os
import json

path = '/Users/xingfeng/Java/dos'
files = os.listdir(path)
files.sort()
par_file = open("/Users/xingfeng/Java/parse_json.json","w+")
# par_file2 = open("/Users/xingfeng/Java/parser_json.json","w+")
index = 1

def load(f_path):
    # with open(f_path,"r+") as f:
    #     print(f_path)
    #     for line in f.readlines():
    #         string = ""
    #         line = "".join(line.split())
    #         string = string + line
    #     string = string.replace('\'','\"')
    #     par_file.write(string)    
    #     par_file.write("\n")
    string = ""
    global index

    f = open(f_path)
    js = json.load(f)
    for item in js:
        if item != None:
            dic = {"index":{"_id":str(index)}}
            index = index + 1
            par_file.write(str(dic))
            par_file.write("\n")
            par_file.write(str(item))
            par_file.write("\n")


    # for line in open(f_path,"r+"):
    #     string = ""
    #     line = "".join(line.split())
    #     string = string + line
    # string = string.replace('\'','\"')
    # par_file.write(string)    
    # par_file.write("\n")



def parse():
    # index = 1
    for file in files:
        if file[-1]!="n":
            continue
        # dic = {"index":{"_id":str(index)}}
        # index = index + 1
        # par_file.write(str(dic))
        f_path = path + "/" +file
        # par_file.write("\n")
        print(file)
        load(f_path)

def func():
    with open('/Users/xingfeng/Java/parse_json.json','r+') as f:
        for line in f.readlines():
            par_file2.write(line.replace('\'','\"'))




if __name__ == "__main__":
    parse()
    # func()