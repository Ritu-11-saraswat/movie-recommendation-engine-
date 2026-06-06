MOVIES = [
    # Bollywood
    {"title": "Dilwale Dulhania Le Jayenge", "year": 1995, "industry": "Bollywood", "genre": ["Romance", "Drama"], "mood": ["Happy", "Romantic"], "rating": 8.1, "description": "A young man follows the love of his life to her home in India."},
    {"title": "3 Idiots", "year": 2009, "industry": "Bollywood", "genre": ["Comedy", "Drama"], "mood": ["Happy", "Motivational"], "rating": 8.4, "description": "Two friends search for their third buddy who inspired them."},
    {"title": "Dangal", "year": 2016, "industry": "Bollywood", "genre": ["Drama", "Sports"], "mood": ["Motivational", "Emotional"], "rating": 8.3, "description": "A father trains his daughters to become world-class wrestlers."},
    {"title": "Kabir Singh", "year": 2019, "industry": "Bollywood", "genre": ["Romance", "Drama"], "mood": ["Sad", "Emotional"], "rating": 7.1, "description": "A talented surgeon's life spirals after a painful breakup."},
    {"title": "Andhadhun", "year": 2018, "industry": "Bollywood", "genre": ["Thriller", "Crime"], "mood": ["Thrilling", "Dark"], "rating": 8.2, "description": "A blind pianist witnesses a murder and gets entangled in a web."},
    {"title": "Gully Boy", "year": 2019, "industry": "Bollywood", "genre": ["Drama", "Music"], "mood": ["Motivational", "Happy"], "rating": 7.9, "description": "A street rapper from the slums of Mumbai rises to fame."},
    {"title": "Queen", "year": 2014, "industry": "Bollywood", "genre": ["Drama", "Comedy"], "mood": ["Happy", "Motivational"], "rating": 8.1, "description": "A solo honeymoon changes a jilted bride's life forever."},
    {"title": "Tumbbad", "year": 2018, "industry": "Bollywood", "genre": ["Horror", "Fantasy"], "mood": ["Dark", "Thrilling"], "rating": 8.2, "description": "A man's obsession with ancient treasure consumes generations."},
    {"title": "Zindagi Na Milegi Dobara", "year": 2011, "industry": "Bollywood", "genre": ["Adventure", "Comedy"], "mood": ["Happy", "Motivational"], "rating": 8.1, "description": "Three friends go on a road trip across Spain before one gets married."},
    {"title": "Gangs of Wasseypur", "year": 2012, "industry": "Bollywood", "genre": ["Crime", "Drama"], "mood": ["Dark", "Thrilling"], "rating": 8.2, "description": "A saga of revenge and power in the coal mines of Dhanbad."},
    {"title": "Dil Chahta Hai", "year": 2001, "industry": "Bollywood", "genre": ["Comedy", "Romance"], "mood": ["Happy", "Nostalgic"], "rating": 8.1, "description": "Three best friends navigate love, life, and friendship."},
    {"title": "Taare Zameen Par", "year": 2007, "industry": "Bollywood", "genre": ["Drama"], "mood": ["Emotional", "Motivational"], "rating": 8.4, "description": "A dyslexic child finds hope through an understanding art teacher."},
    {"title": "Stree", "year": 2018, "industry": "Bollywood", "genre": ["Horror", "Comedy"], "mood": ["Happy", "Thrilling"], "rating": 7.8, "description": "A small town is haunted by a ghost that takes men away."},
    {"title": "PK", "year": 2014, "industry": "Bollywood", "genre": ["Comedy", "Drama"], "mood": ["Happy", "Emotional"], "rating": 8.1, "description": "An alien stranded on Earth questions India's religious practices."},
    {"title": "Brahmastra", "year": 2022, "industry": "Bollywood", "genre": ["Action", "Fantasy"], "mood": ["Thrilling", "Happy"], "rating": 5.6, "description": "A young man discovers his unique power connected to the Brahmastra."},

    # Hollywood
    {"title": "The Dark Knight", "year": 2008, "industry": "Hollywood", "genre": ["Action", "Thriller"], "mood": ["Dark", "Thrilling"], "rating": 9.0, "description": "Batman battles the Joker who plunges Gotham into chaos."},
    {"title": "Interstellar", "year": 2014, "industry": "Hollywood", "genre": ["Sci-Fi", "Drama"], "mood": ["Emotional", "Thrilling"], "rating": 8.6, "description": "Astronauts travel through a wormhole to save humanity."},
    {"title": "The Shawshank Redemption", "year": 1994, "industry": "Hollywood", "genre": ["Drama"], "mood": ["Motivational", "Emotional"], "rating": 9.3, "description": "A banker finds hope and friendship in prison over decades."},
    {"title": "Inception", "year": 2010, "industry": "Hollywood", "genre": ["Sci-Fi", "Thriller"], "mood": ["Thrilling", "Dark"], "rating": 8.8, "description": "A thief who steals secrets through dream-sharing tech."},
    {"title": "The Pursuit of Happyness", "year": 2006, "industry": "Hollywood", "genre": ["Drama"], "mood": ["Motivational", "Emotional"], "rating": 8.0, "description": "A struggling salesman raises his son while chasing success."},
    {"title": "Avengers: Endgame", "year": 2019, "industry": "Hollywood", "genre": ["Action", "Sci-Fi"], "mood": ["Thrilling", "Emotional"], "rating": 8.4, "description": "The Avengers assemble one last time to reverse Thanos's actions."},
    {"title": "La La Land", "year": 2016, "industry": "Hollywood", "genre": ["Romance", "Musical"], "mood": ["Romantic", "Nostalgic"], "rating": 8.0, "description": "An aspiring actress and jazz musician fall in love in LA."},
    {"title": "Parasite", "year": 2019, "industry": "Hollywood", "genre": ["Thriller", "Drama"], "mood": ["Dark", "Thrilling"], "rating": 8.5, "description": "A poor family schemes to become employed by a wealthy household."},
    {"title": "Home Alone", "year": 1990, "industry": "Hollywood", "genre": ["Comedy"], "mood": ["Happy", "Nostalgic"], "rating": 7.7, "description": "A boy is accidentally left home alone and must defend it from burglars."},
    {"title": "The Notebook", "year": 2004, "industry": "Hollywood", "genre": ["Romance", "Drama"], "mood": ["Romantic", "Sad"], "rating": 7.8, "description": "An old man reads a love story to a woman with dementia."},
    {"title": "Get Out", "year": 2017, "industry": "Hollywood", "genre": ["Horror", "Thriller"], "mood": ["Dark", "Thrilling"], "rating": 7.7, "description": "A Black man uncovers a disturbing secret at his girlfriend's family home."},
    {"title": "Forrest Gump", "year": 1994, "industry": "Hollywood", "genre": ["Drama", "Comedy"], "mood": ["Happy", "Emotional"], "rating": 8.8, "description": "A kind-hearted man witnesses and influences major historical events."},
    {"title": "The Lion King", "year": 1994, "industry": "Hollywood", "genre": ["Animation", "Drama"], "mood": ["Emotional", "Motivational"], "rating": 8.5, "description": "A young lion prince flees after his father's murder."},
    {"title": "Spider-Man: No Way Home", "year": 2021, "industry": "Hollywood", "genre": ["Action", "Sci-Fi"], "mood": ["Thrilling", "Emotional"], "rating": 8.2, "description": "Spider-Man faces villains from alternate universes."},
    {"title": "Joker", "year": 2019, "industry": "Hollywood", "genre": ["Drama", "Thriller"], "mood": ["Dark", "Sad"], "rating": 8.4, "description": "A failed comedian descends into madness and becomes a symbol of rebellion."},
]

GENRES = sorted(set(g for movie in MOVIES for g in movie["genre"]))
MOODS = sorted(set(m for movie in MOVIES for m in movie["mood"]))
