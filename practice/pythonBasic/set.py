#print a set item by loop;
myset= {"arif","sagor", "rifat", "akas"};# in set duplicate not allow
# for name in myset:
#     print(name);

#is a aliment available in set
print("arif" in myset)

#accces a item; first it convert in list
print(list(myset)[3])
print(myset)

# add a item in set
myset.add("ratul")
print(myset);# it add a item in first index;{'ratul', 'sagor', 'akas', 'arif', 'rifat'}

# join or update set 
seconSet= ("a", "b", "c", "d");# 
myset.update(seconSet)
print(myset);#{'c', 'sagor', 'rifat', 'd', 'ratul', 'a', 'b', 'arif', 'akas'}  
#note: set will not sequence and unmutable or unchange duplicate not alow


''' delet have for system seconSet.remove("a"), seconSet.discard("a") 
this two systhem should exist 'a' in set or error show

You can also use the pop() method to remove an item, but this method will remove a random item,
so you cannot be sure what item that gets removed.
'''
myset.pop()
print(myset)

#The del keyword will delete the set completely:
del seconSet
#print(seconSet);  finde error when print 

se3 ={"a","b","c","d"}
se4= {"a", "c","f","g"}

se5= se3.union(se4)

print(se5) #{'f', 'd', 'g', 'c', 'b', 'a'}

se3.update(se4); #{'f', 'b', 'g', 'c', 'a', 'd'}
print(se3)
