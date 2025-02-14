'''a={1,2,3,4}
print(type(a)) 
print(a)

a={}#this is empty dict not empty set
print(type(a))

#empty set=
b=set()
print(type(b))
b.add(4)
print(b)'''

#set methods
#add()  remove()  discard()  pop()  clear()  union()  intersection
b={1,2,3,4}
print(len(b))

b.add(8)#cant add list inside the set cant use[] we have to use () cant add dict to set
print(b)
b.remove(4)#removes number
print(b)
b.discard(4)#delets the number
print(b)
b.pop()#b.pop()#this will remove the first element in the set
print(b)

b.union({8,11})
print(b)