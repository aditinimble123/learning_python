# WAP to check if a list contains a palindrome of elements 
# Hint: use copy() Method
#palindrome: same from first and last 
list = [1,2,3,2,1] 
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("The list is palindrome")
else:
    print("The list is not palindrome")    














