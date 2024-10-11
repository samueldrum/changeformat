
"""
Change format library only suport 3 OS

windows - linux

"""

import platform
import subprocess
import warnings

WINDOWS = "windows"

LINUX = "linux"


def install_ffmpeg():

    if platform.platform() == WINDOWS:
        subprocess.run(["winget", "install", "ffmpeg"])

    elif platform.platform() == LINUX: # It's just only for ubuntu based
        subprocess.run(["sudo", "apt", "install", "ffmpeg"])

    warnings.warn("I highly recommend you to restart the ide or code editor that you using now", UserWarning)
    
    




def _change_format(input_file, ouput_file):

    # ffmpeg -i input_file.mp4 output_file.mkv

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, ouput_file])


def _change_format_with_high_quality(input_file, ouput_file):

    # ffmpeg -i input_video.mkv -c:v copy output_video.mp4

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, "-c:v", "copy", ouput_file])
    


def _keeptheaudio(input_file, output_file):
    

    # ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.mp3

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, "-q:a", "0", "-map", "a", output_file])


def _removetheaudio(input_file, output_file):

    # ffmpeg -i input_video.mp4 -an output_video.mp4

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, "-an", output_file])


