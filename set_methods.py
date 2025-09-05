
collection = set() # we"ve created an empty set

# add
collection.add(1)
collection.add("Aditi")
collection.add(34)
print(collection)

# remove
collection.remove(1)
collection.remove(34)
print(collection)

# Clear : empties the set
collection.clear()
print(collection)
print(len(collection))

#pop
collection1 = {1,4,56,767,33,87}
(collection1.pop())
print(collection1)

# Union : combines both set values and returns new
set1 = {1,2,3,4}
set2 = {3,4,5,6,7}
print(set1.union(set2)) # combines set1 and set2
                        # ignore duplicate values

# Intersection : combines common values and returns new
print(set1.intersection(set2))