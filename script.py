def main():
    
    about_me = {
        'name' : 'Brian Casado',
        'student_ID' : '10263301',
        'pizza_toppings' : ['ONIONS', 'BACON', 'ANCHOVIES'],
        'movies' : [
            {
            'title' : 'in time',
            'genre' : 'sci-fi'
            },
            {
            'title' : 'your name',
            'genre' : 'drama'
            }
        ]
    }

    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ['feta', 'ham'])
    print_pizza_toppings(about_me)
    add_movie(about_me, 'bee movie', 'family')
    print_movie_genres(about_me)
    print_movie_titles(about_me)

def print_student_name_and_id(about_me):
   
    first_name=about_me['name'].split()[0]
    print(f"My name is {about_me['name']}, but you can call me Mister {first_name}.")
    print(f"My Student ID is {about_me['student_ID']}.")
    print()

def print_pizza_toppings(about_me):

    print("My favourite pizza toppings are:")
    for topping in about_me['pizza_toppings']:
        print(f"- {topping}")

def add_pizza_toppings(about_me, toppings):

    about_me['pizza_toppings'].extend(toppings)
    for i, toppings in enumerate(about_me['pizza_toppings']):
            about_me['pizza_toppings'][i] = toppings.lower()
    
    about_me['pizza_toppings'].sort()
    print()

def add_movie(about_me, title, genre):
   
   new_movie = {
       'title' : title,
       'genre' : genre
   }
   about_me['movies'].append(new_movie)
   print()


def print_movie_genres(about_me):
 
    movie_genres = [movie['genre'] for movie in about_me['movies']]
    if len(movie_genres) > 1:
        movie_genres[-1] = "and " + movie_genres[-1] 

    print(f"I like to watch {', '.join(movie_genres)}", end=".")
    print()

def print_movie_titles(about_me):
     

    movie_titles = [movie['title'] for movie in about_me['movies']]
    if len(movie_titles) > 1:
        movie_titles[-1] = "and " + movie_titles[-1] 
    
    ##for i, movie_titles in enumerate(about_me['movies']):
    # #       about_me['movies'][i] = movie_titles.capitalize()
    
    print("\n"f"Some of my favourite movies are {', '.join(movie_titles)}", end="!")
    print()

if __name__ == '__main__':
    main()
