def make_album(artist_name, album_title, songs_number=None):
    album_data = {
    'artist name': artist_name.title(),
    'album title': album_title.title()
    }
    if songs_number:
        album_data['songs number'] = songs_number
    return album_data


album_list = []

while True:
    print('Type anytime "q" to quit')
    artist_name = input('Enter the the artist name> ')
    if artist_name == 'q':
        break
    album_title = input("Enter album title> ")
    if album_title == 'q':
        break
    songs_number = input('(Optional) enter number of songs> ')
    if songs_number == 'q':
        break
    album_list.append(make_album(artist_name, album_title, songs_number))

for album in album_list:
    print(album)
