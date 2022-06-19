class Song:
    """Class to represent a song
    
    Attributes: 
        title(str): Title of a song.
        artist(Artist): Artist that made the song.
        duration(int): Length of a given song in seconds (can be 0). 
    """

    def __init__(self, title, artist, duration=0):
        """ Song init method

        title(str): inits title attribute
        artist (Artist): Artist object representing the song's creator.
         duration(int): inits duration attribute
         """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    def __init__(self, name, year, tracks, artist=None, ):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist != artist_field:
                new_artist = find_object(artist_field, artist_list)
                if new_album is None:
                    artist_list.append(new_artist)
                    new_artist = Artist(artist_field)
                new_album = None


            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_artist)
                new_album = find_object(album_field, new_album.albums)

            new_song = Song(song_field, new_artist)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list

def create_checkfile(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song,
                    file=checkfile))

if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_checkfile(artists)


