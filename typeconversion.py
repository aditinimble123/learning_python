#Typeconversion = automatillay converts the datatypes
a = 2
b = 4.25
sum = (a+b) #2.0 + 4.25
print(sum)
print(type(sum)) #here a is converted into float since ans is in float and a is int

#Typecasting = manually we convert i.e jabardasti we do
# it can work on valid types only we cannot add charstring and int or float
d = 1
e = int("2")  # here we did type casting syn: datatype("value")
sum1 = d + e
print(sum1)
print(type(sum1))
