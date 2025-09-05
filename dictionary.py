# Dictionaries are builtin datatype used to store data values in key:value pairs
# They are unordered, mutable(changeable) and dont allow duplicate keys

dict = {
    "Name":"Aditi",
    "CGPA":9.54,
    "marks":[96,97,92,89],
    "Age":19
}
print(dict)           # this will print complete dict
print(dict["Name"])   # this will print oonly name as name is the key and Aditi is the value
print(dict["marks"])  # here marks are the key and the 96,97 etc are the values
print(dict["CGPA"])

# Change the value name
dict["Name"] = "Aditiii"  # Overwrite
print(dict)

# Add the key value pair
dict["Surname"] = "Nimble"
print(dict)

# CRreate a new empty dict
null_dict = {}
print(null_dict)

null_dict["Web Series"] = "Stranger Things" # Add key:value pair in existing null dict
print(null_dict)
