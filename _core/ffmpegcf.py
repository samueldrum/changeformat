
"""
Change format library only support 3 OS

windows - linux - macos

"""

import platform
import subprocess
import warnings

# THE OS SUPPORTED BY changeformat library
WINDOWS = "windows"

MACOS = "darwin"

LINUX = "linux"




def _check_ffmpeg_installed():
    result = subprocess.run(["ffmpeg", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        return True
    else:
        return False



def install_ffmpeg():

    if _check_ffmpeg_installed() == True:
        ...
    else:
        if platform.system().lower() == WINDOWS:
            subprocess.run(["winget", "install", "ffmpeg"])

        elif platform.system().lower() == MACOS:
            subprocess.run(["brew", "install", "ffmpeg"])


        elif platform.system().lower() == LINUX: # It's just only for ubuntu based
            subprocess.run(["sudo", "apt", "install", "ffmpeg"])

        else:
            raise OSError(f"system: {platform.system()} not compatible")

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


