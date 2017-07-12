# jabber=open("sample.txt",'r')
# for line in jabber:
# 	print (line)
# jabber.close()

#
# #using with same as above  but preferrable
#
# with open("sample.txt",'r') as jabber:
# 	for line in jabber:
# 		print(line,end='')
# jabber.close()

# #using readline
#
#
# with open("sample.txt",'r') as jabber:
# 	line=jabber.readline()
# 	while line:
# 		print(line,end='')
# 		line=jabber.readline()
# jabber.close()

# #using readlines
#
# with open("sample.txt",'r') as jabber:
# 	lines=jabber.readlines()
# for  line in lines :
# 	print(line,end='')
#
# jabber.close()

#using readlines with slice to read in reverse

#
# with open("sample.txt",'r') as jabber:
# 	lines=jabber.readlines()  #converts the file into a list
# for  line in lines[::-1] :
# 	print(line,end='')
#
# for  line in lines:
# 	print(line,end='')
# jabber.close()


#using read


with open("sample.txt",'r') as jabber:
	lines=jabber.read()  
for  line in lines[::-1] :
	print(line,end='')

for  line in lines:
	print(line,end='')
jabber.close()
