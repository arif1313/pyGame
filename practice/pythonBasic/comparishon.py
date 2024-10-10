#comparishon 
array=[2,5,24,7,83,9,3]

double_arry= [item*2 for item in array]
print(double_arry)

#sort list
array.sort()
print(array)
array2= [52,84,65,236,14]
# Sort the list descending:
array2.sort(reverse=True)
print(array2)

nameList= ["Arif", "Sagor", "Rifat", "Ruma", "chadni", "Doli","Choity"];
nameList.sort()
print(nameList); #  sort function is case sensetive so  Output = ['Arif', 'Choity', 'Doli', 'Rifat', 'Ruma', 'Sagor', 'chadni']

'''
by default key set. you can do sort case Insensetive by customize ke

'''
nameList.sort(key=str.lower);

print(nameList);# now output is ['Arif', 'chadni', 'Choity', 'Doli', 'Rifat', 'Ruma', 'Sagor']




