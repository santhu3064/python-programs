# ipaddress = input("Enter ip address of computer \n")
# count = 0
# j=0
# for i in range(0,len(ipaddress)):
# 	if ipaddress[i] in ("."):
# 		count += 1
# 		print (ipaddress[j:i])
# 		j = i+1
# print ("number of segments are {0} " .format(count+1))

ipaddress = str(input("Enter ip address of computer \n"))
l=len(ipaddress)
h = ipaddress.split(".",(len(ipaddress)))
k=len(h)
print ("The length of segment is {} " .format(k))
if (k == 4) and (k != l):
	if (len(h[0]) != 3):
		print("Invalid first segment value")
	else:
		for i in range(1,len(h)):
			m = len(h[i])
			if(m > 0) and (m <= 3):
				print (h[i])
			else:
				print("Invalid ip adress in segment {}".format(i))
else:
	print("invalid ip")



















# 		print ("invalid")
#     else:
# 		for i in range(len(h)):
# 			print (h[i])
# else:
# print ("hi")