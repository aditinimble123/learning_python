#concatenation
str1 = "Aditi"
str2 = "Nimble"
final_str = str1 + " " + str2 #adding some space formatting
print(final_str)   # by storing it first in final string then prininting it
len2 = len(final_str) # imp : spaces also get count in lenghth
print(len2)
print(str1+str2)  #direct operation


# length of string .... len(str)
str3 = "television"
len3 = len(str3)
print(len3)  


# Indexing 
# A D I T I _ N I M B  L  E
# 0 1 2 3 4 5 6 7 8 9 10 11
str4 = "Aditi Dattatray Nimble"

#Accessing element from the string. you cannot modify elements
ch = str4[0]   # first store then print
print(ch)
print(str4[4])  # direct write 

# Slicing: accessing parts of a string
# syn: str[staring_index:Ending_index]
str5 = "Barbie girl"
print(str5[1:4])  # arb will slice . last one dont count
print(str5[:6])  #you can skip writing first index [0:6]
print(str5[6:])  #you can skip writing last index  [6:10]
print(str5[6:len(str5)]) # you can also write lenof for slicing till last

# Negative index Slicing
# A  P  P  L  E
#-5 -4 -3 -2 -1 
str6 = "APPLE"
print(str6[-3:-1]) #"pl"










