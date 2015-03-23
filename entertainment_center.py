import media, fresh_tomatoes, urllib2, json

moviesCollection = {'tt0114709':media.Movie(), 'tt2015381':media.Movie(), 'tt0091042':media.Movie(), 'tt0082971':media.Movie(), 'tt1049413':media.Movie(), 'tt0076759':media.Movie()}

movies=[]

for x in moviesCollection:
	req = urllib2.Request('http://www.omdbapi.com/?i={0}&plot=short&r=json'.format(x))
	response = urllib2.urlopen(req)
	movie_data = json.load(response)
	moviesCollection[x].title = movie_data["Title"]
	moviesCollection[x].storyline = movie_data["Plot"]
	moviesCollection[x].poster = str(movie_data["Poster"])
	moviesCollection[x].imdb_url = "http://www.imdb.com/title/{0}/".format(x)
	
	

# toy_story = media.Movie("Toy Story", "A story about a boy and his toys that come to life", 
						# "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						# "https://www.youtube.com/watch?v=vwyZH85NQC4",
						# "http://www.imdb.com/title/tt0114709/")


# gotg = media.Movie("Guardians of the Galaxy",
					 # "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",
					 # "http://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
					 # "https://www.youtube.com/watch?v=B16Bo47KS2g",
					 # "http://www.imdb.com/title/tt2015381/?ref_=nv_sr_1")

# ferrisBueller = media.Movie("Ferris Bueller's Day Off",
							# "A high school wise guy is determined to have a day off from school, despite what the principal thinks of that.",
							# "http://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg",
							# "https://www.youtube.com/watch?v=R-P6p86px6U",
							# "http://www.imdb.com/title/tt0091042/?ref_=nv_sr_1")

# indianaJones = media.Movie("Indiana Jones and the Raiders of the Lost Ark", 
						   # "Archaeologist and adventurer Indiana Jones is hired by the US government to find the Ark of the Covenant before the Nazis.",
						   # "http://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg",
						   # "www.youtube.com/watch?v=gz4crpFaW4M",
						   # "http://www.imdb.com/title/tt0082971/?ref_=fn_al_tt_1")

# up = media.Movie("Up", 
				 # "To avoid being taken away to a nursing home, an old widower tries to fly his home to Paradise Falls, South America, along with a boy scout who accidentally lifted off with him.",
				 # "http://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
				 # "https://www.youtube.com/watch?v=pkqzFUhGPJg",
				 # "http://www.imdb.com/title/tt1049413/?ref_=fn_al_tt_1")

# starWars = media.Movie("Star Wars: Episode IV - A New Hope", "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the universe from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
							 # "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
							 # "https://www.youtube.com/watch?v=9gvqpFbRKtQ",
							 # "http://www.imdb.com/title/tt0076759/?ref_=nv_sr_2")
for x in moviesCollection:
	movies.append(moviesCollection[x])
#movies = [toy_story, gotg, ferrisBueller, indianaJones, up, starWars]
fresh_tomatoes.open_movies_page(movies)
