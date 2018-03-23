my_movies = {'The Saint', '5th Element', 'Ace Ventura', 'Forrest Gump'}

friends_movies = {'Independence Day', 'Ferris Buelers Day Off', 'Major League', 'Forrest Gump'}

def common_movies(movie_list1, movie_list2):
    if len(my_movies & friends_movies) > 0:
        print('These are the movies in common:\n')
    for movie in (movie_list1 & movie_list2):
        print('movie')
    else:
        print('There are no movies in common:\n')


common_movies(my_movies, friends_movies)
