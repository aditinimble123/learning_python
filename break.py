tup = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found at index ",i)
        break
    i += 1
print("end of loop")


j = 0
while j <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1









