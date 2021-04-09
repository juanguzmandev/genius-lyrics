#Ejemplo de listas en Python
import requests
import lyricsgenius as lg
import sys
from colorama import init
from colorama import Fore, Back, Style

#Initializing text coloring
init()

#Genius API Token

TOKEN = 'DQPh7leID-YeyhqMv5PzY1kQpDI33m-rHKFByovnHCDd5pB8YFaAAJBUuK4y8ybI'

#Connecting to Genius API
genius = lg.Genius(TOKEN)

#Receiving song's name and artist
artist_name = input('Nombre del artista:\n')
song_name = input('Nombre de la cancion:\n')

#Looking for desired song
song = genius.search_song(song_name, artist_name)

#Getting the lyrics
lyrics = song.lyrics

#Giving color to lyrics
colored_lyrics = Fore.GREEN + Style.BRIGHT + lyrics

#Printing and giving some color
print(colored_lyrics) 

