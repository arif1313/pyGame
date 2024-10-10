# def summetion(a, b):
#     x= a+b
#     print(x);
# summetion(3,6);
# b=input();
# a= input();

# summetion(float(a),float(b));

# return type function
# def returfun (a, b):
#     return a*b;

# b=input();
# a= input();
# x=returfun(float(a),float(b));

# print(x);


# lamda function
a=3
b=5
lamdaAccess=lambda a,b :\
    a+b;
print(lamdaAccess(a,b))

#function and lamda function 

def myfun(n):
    return lambda a: a*n;
multiple= myfun(2); #pass function parameter
result = multiple(11);# pass lamda function parameter
print(result);






