# from album import *
# from song import *


class Band:

    def __init__(self, name: str,):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_names = [album.name for album in self.albums]
        if album_name not in album_names:
            return f"Album {album_name} is not found."
        album = self.albums[album_name.index(album_name)]
        if album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        band = f"Band {self.name}\n"
        albums = [album.details() for album in self.albums]
        return band + "\n".join(albums)



# song = Song("A", 3.15, False)
# message = song.get_info()
# expected = "A - 3.15"
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# message = album.details()
# expected = "Album The Sound of Perseverance\n"
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, False)
# message = album.add_song(song)
# expected = "Song Scavenger of Human Sorrow has been added to the album The Sound of Perseverance."
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, False)
# album.add_song(song)
# message = album.add_song(song)
# expected = "Song is already in the album."
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, True)
# message = album.add_song(song)
# expected = "Cannot add Scavenger of Human Sorrow. It's a single"
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, False)
# album.publish()
# message = album.add_song(song)
# expected = "Cannot add songs. Album is published."
# print(message)
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, False)
# album.add_song(song)
# message = album.remove_song("Scavenger of Human Sorrow")
# expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, False)
# message = album.remove_song("Scavenger of Human Sorrow")
# expected = "Song is not in the album."
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, False)
# album.add_song(song)
# album.publish()
# message = album.remove_song("Scavenger of Human Sorrow")
# expected = "Cannot remove songs. Album is published."
# print(message)
#
#
#
# album = Album("The Sound of Perseverance")
# message = album.publish()
# expected = album.published
# print(message)
#
#
#
# album = Album("The Sound of Perseverance")
# message = album.publish()
# expected = "Album The Sound of Perseverance has been published."
# print(message)
#
#
# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, False)
# album.add_song(song)
# message = album.details()
# expected = "Album The Sound of Perseverance\n== Scavenger of Human Sorrow - 6.56\n"
# print(message)
#
#
#
# band = Band("Death")
# message = f"{band.name} - {len(band.albums)}"
# expected = "Death - 0"
# print(message)
#
#
#
# band = Band("Death")
# album = Album("The Sound of Perseverance")
# message = band.add_album(album)
# expected = "Band Death has added their newest album The Sound of Perseverance."
# print(message)
#
#
#
# band = Band("Death")
# album = Album("The Sound of Perseverance")
# band.add_album(album)
# message = band.add_album(album)
# expected = "Band Death already has The Sound of Perseverance in their library."
# print(message)
#
#
#
# band = Band("Death")
# album = Album("The Sound of Perseverance")
# band.add_album(album)
# message = band.remove_album("The Sound of Perseverance")
# expected = "Album The Sound of Perseverance has been removed."
# print(message)
#
#
#
# band = Band("Death")
# album = Album("The Sound of Perseverance")
# message = band.remove_album("The Sound of Perseverance")
# expected = "Album The Sound of Perseverance is not found."
# print(message)
#
#
#
# band = Band("Death")
# album = Album("The Sound of Perseverance")
# album.publish()
# band.add_album(album)
# message = band.remove_album("The Sound of Perseverance")
# expected = "Album has been published. It cannot be removed."
# print(message)
#
# band = Band("Death")
# message = band.details()
# expected = "Band Death\n"
# print(message)