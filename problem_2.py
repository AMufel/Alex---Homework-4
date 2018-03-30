my_movies = {'The Saint', '5th Element', 'Ace Ventura', 'Forrest Gump'}

friend_movies = {'Independence Day', 'Ferris Buelers Day Off', 'Major League', 'Forrest Gump'}

common_movies = my_movies.intersection(friend_movies)
only_mymovies = my_movies.difference(friend_movies)
print(common_movies)
print(friend_movies)
