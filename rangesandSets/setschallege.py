value=input("pLease enter a sentence or word \n")
vowel={"a","e","i","o","u","A","E","I","O","U"}

initset=set()
h=set(value)
print (h)
for i  in value:
	initset.add(i)
print (initset)
print ("the words which are not vowels in the gvien sentence are {} \n" .format(initset -vowel))