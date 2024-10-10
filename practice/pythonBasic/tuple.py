#extract tuple or unpack tuple
tuple1= ("rafiq", "karim","rahim")
(friend, cousin, brother)= tuple1
print(friend)
print(cousin)
print(brother)
'''if you Astaric any name it will be a arry of many element that will not declard by name'''
tuple2= ("rafiq", "karim","rahim", "khadija", "akter", "rita")
(first, second, third, *other)= tuple2
print(first)
print(second)
print(third)
print(other)

#tuple join tuple do not have extend tunction for join two use + sign 
tuple3= tuple1 + tuple2
print(tuple3)