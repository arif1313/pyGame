thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# access dictonary 
print(thisdict["brand"])
print(thisdict.get("brand")) # this two output are same
print(thisdict.keys()); # output all keys ar available 
print(thisdict.values()) # output all value are in the dictonary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

x=myfamily["child1"].values()
print(x)
y= myfamily["child2"]["year"]
print(y)
print(myfamily)

myfamily["child1"]["name"]="arif"
print(myfamily)
#update method

myfamily["child2"].update({"home":"barishal", "hsc":"hatemali"})
print(myfamily)
myfamily["child2"].pop("hsc")
print(myfamily)
'''also can your del myfamily["children"],
 for remove alll can your del myfamily or myfamily.clear()'''


# made a dict by two tuple 
tup1=("name", "home")
tup2=("arif", "barishal")


mydict= dict.fromkeys(tup1, tup2)
print(mydict)