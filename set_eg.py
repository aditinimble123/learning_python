# ---- Set Example ----
fruits = {"apple", "banana", "mango"}
print("\nFruits Set:", fruits)

# Add a fruit
fruits.add("orange")
print("After adding orange:", fruits)

# Remove a fruit
fruits.remove("banana")
print("After removing banana:", fruits)

# Set operations
tropical = {"mango", "orange", "pineapple"}
print("\nTropical fruits:", tropical)

print("Union:", fruits | tropical)          # all unique fruits
print("Intersection:", fruits & tropical)   # common fruits
print("Difference:", fruits - tropical)     # fruits only in 'fruits'