student = {
    "name":"Aditi Nimble",
    "subjects": {
        "phy": 97,
        "Chem": 95,
        "math": 99,
        "Bee": 92,
        "fpl": 100,
    }
}

print(student.keys()) # it will write the keys of dict

print(list(student.keys())) # convert it into list

print(len(student))

print(student.values()) # it will print the values of dict

print(list(student.values()))

print(student.items()) # it will print both key:value pairs in the form of tuple

print(student.get("name")) # it will print value of key

print(student["name"]) # it will also print the value of key

new_dict = {"city":"Lonavala"}
student.update(new_dict) # update the key value pair 
print(student)





