from itunes_module import artist_songs

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