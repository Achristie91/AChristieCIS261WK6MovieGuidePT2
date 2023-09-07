def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()
    
def list_movies(movies):
    for i, movie in enumerate(movies,  start=1):
        print(f"{i}. {movie}")
    print()
    
def add_title(movie_list, new_title):
    movie_list.append(new_title)
    print("Movie title added successfully.")
    
def delete(movie_list):
    number = int(input("Number:  "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number. \n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was deleted. \n")
    
def write_to_file(movie_list):
    with open("movies.txt.", "w") as file:
        for title in movie_list:
            file.write(title + "\n")
        
def main(new_title=None):
    movie_list  = []
    
    with open("movies.txt", "w") as file:
        file.write("Cat on a Hot Tin Roof\nOn the Waterfront\nMonty Python and the Holy Grail\n")  

    display_menu()
    
    while True:
        command = input("Command:  ")
        if command.lower() == "list":
            list(movie_list)   
        elif  command.lower() == "add":
            add_title(movie_list, new_title)
            add_title(movie_list, new_title)
            write_to_file(movie_list)
            display_titles(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Later!")
    
if __name__ == "__main__":
    main()