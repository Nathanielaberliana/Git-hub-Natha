def make_album(artist, title, songs=None):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if songs:
        album_dict['songs'] = songs
    return album_dict

album = make_album('kereta kencan', 'hivi!')
print(album)

album = make_album('tulus', 'monokrom')
print(album)

album = make_album('raisa', 'heart to heart')
print(album)

album = make_album('tulus', 'gajah', songs=10)
print(album)
