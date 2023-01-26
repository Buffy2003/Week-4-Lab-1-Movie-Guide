# Rashelle Ward
# CIS261
# Movie List Program

def display_menu():
    print("The Movie List Program")
    print()
    print("Command Menu")
    print("List     -   List all movies")
    print("Add      -   Add a movie")
    print("Delete   -   Delete a movie")
    print("Exit     -   Exit program")
    print()

def list(movieList):
    for i, movie in enumerate(movieList, start=1):
        print(f"{i}. {movie}")
    print()

def add(movieList):
    movie = input("Movie name: ")
    movieList.append(movie)
    print(f"{movie} has been added.\n")

def delete(movieList):
    number = int(input("Number: "))
    if number < 1 or number > len(movieList):
        print("This is an invalid movie number.\n")
    else:
        movie = movieList.pop(number-1)
        print(f"{movie} has been deleted.\n")

def main():
    movieList = ["Beauty and the Beast", "Bambi", "The Jungle Book"]

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(movieList)
        elif command.lower() == "add":
            add(movieList)
        elif command.lower() == "delete":
            delete(movieList)
        elif command.lower() == "exit":
            break
        else:
            print("This is not a valid command. Please try again.\n")

    print("Good Bye!")


if __name__ == "__main__":
        main()
