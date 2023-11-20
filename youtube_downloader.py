import os
from pytube import YouTube

print(os.getenv('HOME'))

home = os.getenv('HOME')
save_path = home + '/Downloads/'

link = input('Enter URL of YouTube video: ')

try:
    yt = YouTube(link)
except:
    print('Connection error')

mp4files = yt.filter('mp4')

hd-video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)

try:
    hd-video.download(save_path)
except:
    print('Connection error')

print('Download completed')
