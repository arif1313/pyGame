# Python

## print line

```py

print("hello world", end="") #with out new line
print("hello world") #with new line
full_name= "arif hossen "
print(f"hi this is  {full_name}")# with formating
```

## variable declartion and print

```py
name="arif"
age=24
CGPA=3.5
print(name,age,CGPA)#witout formating
print(f"my name is {name}. I am {age} years old. My avarage CGPA is {CGPA}") #for mating system
```

## Type cast

targetType(variable)

```py
amount=5.8
print(int(amount))#float to int
CGPA=4
print(float(CGPA))#int to float
name=str(input())# input string
print(name)
```

## while loop

```
while logic:
    statement 1
    statement 2
```

```py
i=0
while i <10:
    print("my name is arif")
    i=i+1 #pyhon have not increament and decriment operator
```

## for loop

```py
for i in range(10):
    print(i,end=" ")# print 0 to 9
name="md arif howlader "
for i in name:
    print(i,end=" ")# print all letter
```
