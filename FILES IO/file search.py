with open("sample.txt",'r') as jabber:
	lines=jabber.readlines()  #converts the file into a list

for  line in lines:
	if "jabberwock" in line.lower():
		print (line)
	#print(line,end='')
jabber.close()


with open("sample.txt",'r') as jabber:
	 for  line in jabber:
		 if "JAB" in line.upper():
			 print (line)
	#print(line,end='')
jabber.close()



