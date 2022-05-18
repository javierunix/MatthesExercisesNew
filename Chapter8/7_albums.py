def make_album(artist_name, album_title, song_number=None):
    album_data = {
    'artist name': artist_name.title(),
    'album title': album_title.title()
    }
    if song_number:
        album_data['songs number'] = song_number
    return album_data


print(make_album('the doors', 'strange days', 12))
print(make_album('the velvet underground', 'white light, white heat'))
