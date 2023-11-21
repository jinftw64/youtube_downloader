import os
from pytube import YouTube

print(os.getenv('HOME'))

home = os.getenv('HOME')
save_path = home + '/Downloads/'

link = input('Enter URL of YouTube video: ')

try:
    yt = YouTube(link)
    yt.streams.filter(adaptive=True, file_extension='mp4').first().download(output_path=save_path)
except:
    print('Connection error')

print('Download completed')
