class Song:
    count = 0
    artists = []
    genres = []
    genre_count={}
    artist_count={}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if (genre not in Song.genres):
            Song.genres.append(genre)
            Song.genre_count.update({genre : 1})
        else:
            Song.genre_count.update({genre: Song.genre_count[genre]+1})

        if (artist not in Song.artists):
            Song.artists.append(artist)
            Song.artist_count.update({artist: 1})
        else:
            Song.artist_count.update({artist: Song.artist_count[artist] + 1})
    
