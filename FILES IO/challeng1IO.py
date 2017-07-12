for i  in range(2,12):
	for j in range(2,12):
		print ("{0} times {1} is {2}".format(i,j,(i*j)))
	print ("--" * 20)

with open("sample2.txt",'a') as append_file:
	for i  in range(2,12):
		for j in range(2,12):
			print ("{0} times {1} is {2}".format(i,j,(i*j)), file=append_file)
		print (("--" * 20), file=append_file)