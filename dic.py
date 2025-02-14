'''properties:
1.unordered
2.mutable
3.indexed
4.can't contain duplicate keys'''

myDict ={
    "fast":"quick",
    "apple":"fruit",
    "marks":[1,2,3],
    "country":{"india":"delhi"},
    1:2
}

#dict methods
print(myDict['marks'])

print(myDict.keys())

print(type(myDict.keys()))

print(myDict.values())

print(myDict.items())#display (key,value) 

print(myDict)
updateDict ={
    "koti":"animal"
}
myDict.update(updateDict)#updates the key and value
print(myDict)

print(myDict.get("marks"))#this gives none
print(myDict['marks'])#this throws error bcz it is not present