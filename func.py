

par_file2 = open("/Users/xingfeng/Java/parser_json.json","w+")


with open('/Users/xingfeng/Java/parse_json.json','r+') as f:
    for line in f.readlines():
        par_file2.write(line.replace('\'','\"'))
        