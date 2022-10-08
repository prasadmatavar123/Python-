# Length of the set
a = set()
a.add(20)
a.add(30)
a.add(40)
a.add(50)
print(len(a)) #prints the length of the set

#Removal items
b = set()
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add((4,5,6))
b.remove(5)# Removes 5 from set b
print(b)

# pop items
print(b.pop())
print(b) 
 
# clear items
print(b.clear())
print(b) 