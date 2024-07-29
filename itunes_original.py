import requests
def artist_songs(artist, limit):
    """Fetches and prints a list of songs by an artist using the iTunes API."""
    try: 
        itunes = requests.get(f'https://itunes.apple.com/search?term={artist}'
                            f'&limit={limit}&media=music&entity=song')
    except (requests.ConnectionError, requests.Timeout, 
            requests.HTTPError, requests.TooManyRedirects):
        print('A problem has occured.')
    else:
        try:
            # Parse the response JSON content.
            contents = itunes.json()
        except requests.exceptions.JSONDecodeError:
            print('Error decoding JSON.')

    # Iterate through the results and print each song's track name.
    print(f'\nHere are {limit} songs by {artist.title()}: ')
    print('---------------------------------------------------------------')
    for content in contents['results']:
        print(content['trackName'])
    print('---------------------------------------------------------------')

def main():
    """
    Main portion of the program which gets the artist 
    and number of songs from the user.
    """
    while True:

        print('\nEnter \'q\' to quit.')

        # Get artist name from user.
        artist = input('Enter an Artist: ').lower().strip()
        if artist == 'q':
            break

        # Get the number of songs to fetch from the user.
        limit = input('Enter a number of songs: ').lower().strip()
        if limit == 'q':
            break

        try:
            limit = int(limit)
        except ValueError:
            print('Invalid Input. Please enter a number.')
            continue

        # Fetch and print the list of songs for the given artist and limit
        artist_songs(artist, limit)


if __name__ == '__main__':
    main()