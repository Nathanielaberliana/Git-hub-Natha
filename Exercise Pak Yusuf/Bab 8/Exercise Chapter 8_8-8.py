def make_album(artist, title, songs=None):
    """Buat dictionary yang menggambarkan sebuah album musik."""
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album


while True:
    print("\nMasukkan data album (ketik 'q' kapan saja untuk keluar).")

    artist = input("Nama artis: ")
    if artist == 'q':
        break

    title = input("Judul album: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)
    