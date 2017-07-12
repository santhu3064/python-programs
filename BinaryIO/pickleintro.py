import pickle
# imelda=("More Mayhem","Imelda May","2011",((1,"Pullling the rug"),(2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz")))
# with open("imelda_pickle", "bw") as pickle_file:
# 	pickle.dump(imelda,pickle_file)

# with open("imelda_pickle", "br") as pickle_read:
# 	pick_read=pickle.load(pickle_read)
# print(pick_read)
# album,artist,year,track_list =	pick_read
# print (album)
# print(artist)
# print (year)
# print (track_list)
# for i in track_list:
# 	track_number,track_name = i
# 	print (track_name,track_number)
#

#import pickle
imelda=("More Mayhem","Imelda May","2011",((1,"Pullling the rug"),(2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz")))
even=list(range(0,10,2))
odd=list(range(1,10,2))

with open("imelda_pickle", "bw") as pickle_file:
	pickle.dump(imelda,pickle_file, protocol=0)
	pickle.dump(even,pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
	pickle.dump(odd,pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
	pickle.dump(2998302,pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
	pickle.dump("hello",pickle_file, protocol=0)
with open("imelda_pickle", "br") as pickle_read:
	imelda_read=pickle.load(pickle_read)
	even_read=pickle.load(pickle_read)
	odd_read=pickle.load(pickle_read)
	int_read=pickle.load(pickle_read)
	char_read=pickle.load(pickle_read)

print(imelda_read)
album,artist,year,track_list =	imelda_read
print (album)
print(artist)
print (year)
print (track_list)
for i in track_list:
	track_number,track_name = i
	print (track_name,track_number)

print ("==" * 40)
for i in even_read:
	print (i)

print ("==" * 40)
for i in odd_read:
	print (i)

print ("==" * 40)
print (int_read)

print ("==" * 40)
print (char_read)



