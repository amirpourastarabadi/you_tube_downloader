
from colorama import Fore, Back, Style
from pytube import Playlist

link = input('Enter your link and press Enter: ')
p = Playlist(link)

print(f'\nDownloading: {p.title}')

for video in p.videos:
    try:
        stream = video.streams.filter(type='video', resolution='480p', file_extension='mp4')[0]
        print(Fore.WHITE + "\n", stream.title, "...", end="  ")
    except:
        pass
    try:
        stream.download()
        print(Fore.GREEN + u'\u2713')
    except:
        print(Fore.RED + "x")