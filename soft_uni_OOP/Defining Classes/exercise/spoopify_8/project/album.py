class Album:

    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song):
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song_names = [song.name for song in self.songs]
        if song_name not in song_names:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        del self.songs[song_name.index(song_name)]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        album = f"Album {self.name}\n"
        songs = [f"== {song.get_info()}" for song in self.songs]
        return album + "\n".join(songs)
