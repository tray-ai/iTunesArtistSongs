# iTunesArtistSongs
iTunesArtistSongs is a Python application that allows users to search for songs by a specific artist using the iTunes API. Users can specify the number of songs to fetch and the program will display a list of track names. This simple yet powerful tool provides an easy way to explore an artist's discography directly from the command line.

File Descriptions:

`itunes_original.py`:
This script fetches and displays a list of songs by a specified artist using the iTunes API. The user is prompted to enter an artist's name and the number of songs they wish to retrieve. The script handles various exceptions to ensure robust performance, such as connection issues and JSON decoding errors. It then prints the titles of the fetched songs in a formatted manner.

`itunes.py`:
This script is a simplified version that serves as the main program. It imports the `artist_songs` function from an external module (`itunes_module.py`). Like `itunes_original.py`, it prompts the user to enter an artist's name and the number of songs to fetch. It handles user input validation and calls the `artist_songs` function to display the song titles.

`itunes_module.py`:
This module contains the `artist_songs` function, which is responsible for interacting with the iTunes API. It fetches the specified number of songs for a given artist and handles possible errors such as connection issues and JSON decoding errors. The function prints the fetched song titles in a formatted manner. This module is designed to be imported and used by other scripts, such as `itunes.py`.
