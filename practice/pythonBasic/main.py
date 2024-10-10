#my_name = input("what is your name: ")
#print(f"my name is {my_name}")
array= ['arif', 'simul', 'rakib', 'sakib', 'mithon']
'''print(array);
print("okey")
for name in array :
    print(name)
    print("name printed");
i=0;
while(i<3):
    print("while contiue")
    i+=1;
for inx in range(len(array)):
    print(inx);
print(array[2]);
print(array[0:2]);
print(array[:3]);'''
print(array)
array.insert(1, 'sagor')
print(array)
#append method add a array item in last index
array.append("apended")
print(array)
#extend use for add two arry in an aarry item first array will change with two array but second arry will not change
array2=[1,35,67,]
array.extend(array2)
print(array)
print(array2)
# remove operation
# by this method can cahnge one indentify item remove value must be str
array.remove('apended')
print(array)

#pop operation / Pop value will be the index number this way can delete only one value;
array.pop(6)
print(array)

#for delete many 
# deleteItem=[2,4,7];
# for inx in deleteItem:
#      array.pop(inx);
# print(array);

test_list = [5, 6, 3, 7, 8, 1, 2, 10, 5]
indices=[3,7]
 
for i in sorted(indices, reverse=True):
    del test_list[i]
     
print(test_list)

# del method can delete one or more item from list
del array[3:5]
print(array)
#clear for clear all items in list 
test_list.clear()
print(test_list)

#while loop
i=0
while i < len(array):
    print("aray item available")
    i+=1

#short hand for loop 
[print(value) for value in array]










