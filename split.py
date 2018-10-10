
# par_file2 = open("/Users/xingfeng/Java/parser_json.json","r+")

# path = '/Users/xingfeng/Java/dos'

# i = 0

# with open('/Users/xingfeng/Java/parser_json.json','r+') as f:
#     for line in f.readline():
#         par_file2.write(line.replace('\'','\"'))
        

#coding:utf-8

import os

sourceFileName = "/Users/xingfeng/Java/parser_json.json" 
def cutFile():
    
    print("正在读取文件...")
    sourceFileData = open(sourceFileName,'r')
    ListOfLine = sourceFileData.read().splitlines()
    n = len(ListOfLine)
    print("文件共有"+str(n)+u"行")
    print ("请输入需要将文件分割的个数:")
    m = int(raw_input("")) 
    p = n/m + 1
    print("需要将文件分成"+str(m)+u"个子文件")
    print("每个文件最多有"+str(p)+u"行")
    print("开始进行分割···")
    for i in range(m):
        print("正在生成第"+str(i+1)+u"个子文件")
        destFileName = os.path.splitext(sourceFileName)[0]+"_part"+str(i)+".json" 
        destFileData = open(destFileName,"w")
        if(i==m-1):
            for line in ListOfLine[i*p:]:
                destFileData.write(line+'\n')
        else:
            for line in ListOfLine[i*p:(i+1)*p]:
                destFileData.write(line+'\n')
        destFileData.close()
    print("分割完成")

cutFile()