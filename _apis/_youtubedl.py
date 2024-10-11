
from OS import LINUX, MACOS, WINDOWS, detect_system
import subprocess



def __install_youtube_dl():
    system = detect_system().lower()
    if system == WINDOWS:
        print("You might download youtubedl dependency in the official web site")

    elif system == MACOS:
        # brew install youtube-dl
        subprocess. run(["brew", "install", "youtube-dl"])

    elif system == LINUX: # Distro's based on Ubuntu
        # sudo apt install youtube-dl
        subprocess. run(["sudo", "apt", "install", "youtube-dl"])

    else:
        raise OSError("Incompatible System")



def install_youtube_video(link):
    __install_youtube_dl()
    raise NotImplementedError("This function is not implemented yet")

