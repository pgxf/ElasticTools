import numpy
import json
import os
# a = numpy.loadtxt('./7786_pro.json')
# print(size(a))

# list = open('./7786_pro.json','r+').readlines
# print(list[0][0])

# with open('./7786_pro.json','r+') as f:
#     for line in f.readlines():
#         print(line)
#         tmp = json.dumps(line)
#         js = json.load(tmp)
#         print(len(js))

# file = open("./7786_parser.json","w+")


f = open('./7786_pro.json')
js = json.load(f)
print(js)
print(type(js))
print(len(js))
for item in js:
    file.write(str(item))
    file.write('\n')

# file = open("./7786_parser.json","r+")
# for line in file.readline:
#     print(line.replace('\'','\"'))

with open('./7786_parser.json','r+') as f:
    for line in f.readlines():
        f.write(line.replace('\'','\"'))