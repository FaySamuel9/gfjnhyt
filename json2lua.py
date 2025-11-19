# coding=utf-8
import re
import sys

#读取文件
path = "test.json"
if(len(sys.argv) > 1):
    path = sys.argv[1]

f = open(path)
content = f.read()
f.close()

content = re.sub(r'\[', '{', content)

content = re.sub(r']', '}', content)

content = re.sub(r'//', '--', content)

newList = []

#找到所有键
obj = re.compile( r'"[^,]*?:')
list_1 = obj.findall(content)

for s in list_1:
    tmp = '[' + s
    tmp = re.sub(r'"\s*?:', '\"] =', tmp)
    newList.append(tmp)

#将处理后的字符串替换回去
for i in range(len(list_1)):
    content = content.replace(list_1[i], newList[i])

#修正特殊情况，如"key" : "value", "key" : ...
#content = re.sub(r'=\s*?\[\"', '= \"', content)
#content = re.sub(r',\s*\"', ', [\"', content)
#print(content)

#write to a lua file
filename = re.sub(r'\..*$','', path)
f = open(filename + '.lua', 'w')
f.write(content)
f.close()
print("output --> " + filename + '.lua')