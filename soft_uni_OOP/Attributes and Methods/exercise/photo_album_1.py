class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[]for i in range(pages)]
        self.start = 0

    @staticmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        if self.start not in range(self.pages):
            return "No more free spots"
        if len(self.photos[self.start]) == 4:
            self.start += 1
        self.photos[self.start].append(label)
        return f"{label} photo added successfully on page {self.start + 1} slot {len(self.photos[self.start])}"

    def display(self):
        result = [f'{"-" * 11}\n' + len(self.photos[i]) * "[] ".rstrip() for i in range(self.pages) if len(self.photos[i]) != 0]
        return "\n".join(result) + "\n" f'{"-" * 11}'







album = PhotoAlbum(4)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
