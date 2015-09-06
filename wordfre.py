with open("input.txt",'r') as f:
	lines=f.readlines()
	words=[]
	dic={}
	for line in lines:
		words.extend(line.split(" "))
	for word in words:
		word=word.lower()
		if dic.has_key(word):
			dic[word]+=1
		else:
			dic[word]=1

	result=sorted(dic.iteritems(),key=lambda dic:dic[1],reverse=True)
	for i in result[:10]:
		print "word: {0} \ttimes: {1}".format(i[0],i[1])