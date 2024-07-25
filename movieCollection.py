movie_collection = [
    ("Corpse Bride", "Tim Burton", 2005),
    ("Frankenweenie", "Tim Burton", 2012)
]

def add_movie(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)
    print(f"The movie {title} directed by {director} was added to the collection")

def display_movies():
    print("Movie Collection")
    for title, director, year in movie_collection:
        print(f"Title: {title}, Director: {director}, Year: {year}")

    
def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_author, year = movie
        if movie_author.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director

def remove_movie(title):
    for movie in movie_collection:
        if movie[0].lower() == title.lower():
            movie_collection.remove(movie)
            print(f"The movie {title} was removed from collection")
            return
    print(f"The movie {title} was not found in the collection")

def update_movie(title, new_director, new_year):
    for i, movie in enumerate(movie_collection):
        if movie[0].lower() == title.lower():
                movie_collection[i] = (title, new_director, new_year)
                print(f"The movie {title} was updated. Director is now {new_director} and it was released in {new_year}")
                return
    print(f"Could not find the movie {title}")
    
def sort_movies_by_year():
    sorted_collection = sorted(movie_collection, key=lambda movie: movie[2])
    print("Movies sorted by Year:")
    for title, director, year in sorted_collection:
        print(f"Title: {title}, Director: {director}, Year: {year}")

display_movies()

add_movie("Avatar", "James Cameron", 2009)

display_movies()

movies_by_burton = search_by_director("Tim Burton")
print("Movies by Tim Burton:")
for title, director, year  in movies_by_burton:
    print(f"Title: {title}, Year: {year}")

remove_movie("Avatar")


display_movies()
add_movie("Avatar", "James Cameron", 2009)

add_movie("Jamatar", "James Cameron", 2009)

update_movie("Jamatar", "Jayme Chaca", 2024)

display_movies()

sort_movies_by_year()