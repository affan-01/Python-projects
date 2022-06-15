PROMPT = "Press 'A' to add movie to list , Press 'L' to print the list of movies" \
         "Press 'F' to find movies Or Press 'Q' to end menu: "

movie_list = []

def add_movie(name, director):
    movie_list.append({
        'movie_name' : name,
        'director_name': director
    })

def print_list():
    for i in movie_list:
        print(f"title: {i['movie_name']} director_name: {i['director_name']}")

def find_movie(name):
    for i in movie_list:
        if i['movie_name'] == name:
            print("Movie exists in collection")
            break
    else:
        print("Doesnt exist in collection")

selection = input(PROMPT).lower()

while selection != 'q':
    if selection == 'a':
        movie_title = input("Type in movie title: \n")
        director_name = input("Type in director name: \n")
        add_movie(movie_title,director_name)
    elif selection == 'l':
        print_list()
    elif selection == 'f':
        movie_title = input("Enter movie title: \n")
        find_movie(movie_title)
    selection = input(PROMPT).lower()

print("Process termminated")


