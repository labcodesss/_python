L1=[4,7,3,9,6,1,2,0]

#sorting
sorted = L1.sort()
print(sorted)#this gives none
print(L1)
L1.sort()
print(L1)

#reverse
L1.reverse()
print(L1)

#append-- add at end of list
L1.append(5)
print(L1)

#insert
L1.insert(1,56)#here 1 is index that place will be replaced by 56
print(L1)

#pop
L1.pop(5)#5th index will be deleted
print(L1)

#remove
L1.remove(6)
print(L1)