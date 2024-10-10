
"""
Change format library only suport 3 OS

windows - linux

"""

import platform
import subprocess

WINDOWS = "windows"

LINUX = "linux"


def install_ffmpeg():

    if platform.platform() == WINDOWS:
        subprocess.run(["winget", "install", "ffmpeg"])

    elif platform.platform() == LINUX: # It's just only for ubuntu based
        subprocess.run(["sudo", "apt", "install", "ffmpeg"])




def _change_format(input_file, ouput_file):
    # See if ffmpeg it's already installed, if not, it's gonna install it
    install_ffmpeg()
    subprocess.run(["ffmpeg", "-i", input_file, ouput_file])
    

