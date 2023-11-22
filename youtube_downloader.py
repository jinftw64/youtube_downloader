import os
import subprocess
import shlex
from pytube import YouTube

print(os.getenv('HOME'))

home = os.getenv('HOME')
save_path = home + '/Downloads/'

link = input('Enter URL of YouTube video: ')

yt = YouTube(link)

video_streams = yt.streams.filter(adaptive=True, file_extension='webm', type='video')
video_streams = video_streams.first()
video_name = video_streams.default_filename
video_streams.download(output_path=save_path, filename='video.webm')

audio_streams = yt.streams.filter(adaptive=True, file_extension='webm', type='audio')
audio_streams = audio_streams.first()
audio_streams.download(output_path=save_path, filename='audio.webm')

print('Download complete.')

unvalidated_command = f"ffmpeg -i {save_path}video.webm -i {save_path}audio.webm -c copy {save_path}{video_name}.mp4"

escaped_command = shlex.quote(unvalidated_command)

try:
    print('Merging video and audio files...')
    subprocess.run(escaped_command)
except:
    pass

os.remove(f"{save_path}video.webm")
os.remove(f"{save_path}audio.webm")

print('Download completed')
