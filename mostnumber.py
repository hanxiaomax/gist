import random

with open("file.txt",'r') as f:
	lines=f.readlines();
	dic={}
	for line in lines:
		number=line.split(" ")[1].strip('\n')
		name=line.split(" ")[0]
		try:
			dic[number]["names"].append(name)
			dic[number]["count"]+=1
		except :
			dic.setdefault(number,{"names":[name],"count":1})
			
	result=sorted(dic.iteritems(),key=lambda dic:dic[1]['count'],reverse=True)


	print result[0][0]
	for name in result[0][1]["names"]:
		print name