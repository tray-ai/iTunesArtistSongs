import requests

def artist_songs(artist, limit):
    """Fetches and prints a list of songs by an artist using the iTunes API."""
    try: 
        itunes = requests.get(f'https://itunes.apple.com/search?term={artist}'
                            f'&limit={limit}&media=music&entity=song')
        
        # Parse the response JSON content.
        contents = itunes.json()
    except (requests.exceptions.RequestException, 
            requests.exceptions.JSONDecodeError):
        print('A problem has occured.')

    # Iterate through the results and print each song's track name.
    print(f'\nHere are {limit} songs by {artist.title()}: ')
    print('---------------------------------------------------------------')
    for content in contents['results']:
        print(content['trackName'])
    print('---------------------------------------------------------------')