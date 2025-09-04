# WAP to ask the user to enter names of their 3 favourite movies and store them in list
print("Enter your three favorite movies:")
movies = []
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2nd movie: ")
mov3 = input("Enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)


# Direct append and take input
movies.append(input("Enter 1st movie:"))
movies.append(input("Enter 2nd movie:"))
movies.append(input("Enter 3rd movie:"))
print(movies)