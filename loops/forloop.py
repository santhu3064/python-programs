number="1,456,876,098,776,994,778"
#for i in range(0,len(number)):
for i in range(len(number)):
	if number[i] in "012345678":
		 #print ("the number {0} in given number {1} is {2}".format(i,number,number[i]))
		 print (number[i],end='') #changing deafult seperatoe for for loop using end
print ("\n")


number="1,456,876,098,776,994,778"
cleannumber=''
#for i in range(0,len(number)):
for i in range(len(number)):
	if number[i] in "012345678":
		cleannumber = cleannumber + number[i] #cleannumber += number[i]
newnumber = int(cleannumber)
print (newnumber)

a="hello howa re you"
for h in a:
	print (h,end=":")


a="hello howa re you"
for h in a:
	print ("the word is " , h)
	print ("the word is "  + h)



