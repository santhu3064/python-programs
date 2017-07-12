# with open("binary","bw") as bin_file:
# 	for i in range(17):
# 		bin_file.write(bytes([i]))
# with open("binary","br") as bin_read:
# 	for i in bin_read:
# 		print(i)

a=65534
b=65535
c=65536
d=2998302

with open("binary_2","bw") as binary_file:
	binary_file.write(a.to_bytes(2,"big"))
	binary_file.write(b.to_bytes(2,"big"))
	binary_file.write(c.to_bytes(4,"big"))
	binary_file.write(d.to_bytes(4,"big"))
	binary_file.write(d.to_bytes(4,"little"))

with open("binary_2","br") as binary_read:
	for i in binary_read:
		print(i)

with open("binary_2","br") as binary_read:
	e=int.from_bytes(binary_read.read(2),"big")
	print (e)
	f=int.from_bytes(binary_read.read(2),"big")
	print (f)
	g=int.from_bytes(binary_read.read(4),"big")
	print (g)
	h=int.from_bytes(binary_read.read(4),"big")
	print (h)
	i=int.from_bytes(binary_read.read(4),"little")
	print (i)
