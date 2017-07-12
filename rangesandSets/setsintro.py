farm_animals={"sheep","cow","dog"}
jungle_animals=set(["wolf","lion","tiger","elephant"])
print (farm_animals)
print (jungle_animals)
farm_animals.add("horse")
print (farm_animals)
union1=set(range(2,20,3))
union2=set(range(21,40,3))
a=sorted(union2.union(union1))
print (a)
union3={"a","b","c"}

#b=union2.union(union3)
#print (b)
c=set(range(0,40,4))
print (c)
a=set(range(2,20,2))
print("intersection")
print (c.intersection(a))
#print(c & a)
print ("c minus a")
print ( c - a )
print ("a minus c")
print (a - c)
print ( a.difference(c))
print(c.difference(a))
a.difference_update(c)
print (sorted(a))
a.remove(2)
a.discard(3)

try:
 a.remove(100)
except KeyError:
 print("The index is  not present")


a.discard(100)
