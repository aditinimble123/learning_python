# WAP to find the greatest of 3 numbers entered by the user.
n1 = input("Enter the first no: ")
n2 = input("Enter the second no: ")
n3 = input("Enter the third no: ")
if(n1 > n2 and n1 > n3):
    print("The greatest is",n1)
elif(n2 > n3 and n2 > n1):
    print("The greatest is",n2)
else:
    print("The greatest is",n3)        
