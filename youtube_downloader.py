import os
import sys
import subprocess
import shlex
from pytube import YouTube

def getSavePath():
    home = os.getenv('HOME')
    return home + '/Downloads/'

def download():
    save_path = getSavePath()
    link = input('Enter URL of YouTube video: ')

    # create YouTube object
    yt = YouTube(link)

    try:
        # filter by adaptive streams (seperate video and audio tracks)
        # select the highest quality video
        video_streams = yt.streams.filter(adaptive=True, file_extension='webm', type='video')
        video_streams = video_streams.first()

        # create video name without extension
        video_name = video_streams.default_filename
        video_name = video_name.split('.')[0]

        # download video
        video_streams.download(output_path=save_path, filename='video.webm')
    except Exception as e:
        print(f"Error while downloading video stream: {e}")
        sys.exit(1)

    try:
        # filter by adaptive streams (seperate video and audio tracks)
        # select the highest quality audio
        audio_streams = yt.streams.filter(adaptive=True, file_extension='webm', type='audio')
        audio_streams = audio_streams.first()

        # download audio
        audio_streams.download(output_path=save_path, filename='audio.webm')
    except Exception as e:
        print(f"Error while downloading audio stream: {e}")
        sys.exit(1)

    print('Success! Downloaded video and audio stream.')

def getFilePaths():
    save_path = getSavePath()
    video_path = save_path + 'video.webm'
    audio_path = save_path + 'audio.webm'
    return video_path, audio_path

def merge(filepath1, filepath2, destination):
    command = ['ffmpeg', '-i', '{}video.webm'.format(save_path), '-i', '{}audio.webm'.format(save_path), '-c', 'copy', '{}'.format(save_path) + '{}.mp4'.format(shlex.quote(video_name)) ]

    try:
        print('Merging video and audio files...')
        subprocess.run(command)
    except:
        pass

    # os.remove(f"{save_path}video.webm")
    # os.remove(f"{save_path}audio.webm")

    print('Download completed')
