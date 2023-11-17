import os
from pytube import YouTube

print(os.getenv('HOME'))

home = os.getenv('HOME')
save_path = home + '/Downloads/'

link = input('Enter URL of YouTube video: ')

try:
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
except:
    print('Connection error')

try:
    yt.download(save_path)
except:
    print('Connection error')

print('Download completed')
