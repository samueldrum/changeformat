
from OS import LINUX, MACOS, WINDOWS, detect_system, platform
import subprocess


# Not supported on windows
if detect_system().lower() == WINDOWS:
    raise OSError(f"{platform()} is not compatible with youtubedl api, try WSL")



def __install_youtube_dl():
    system = detect_system().lower()
    if system == WINDOWS:
        print("You might download youtubedl dependency in the official web site")

    elif system == MACOS:
        # brew install youtube-dl
        subprocess. run(["brew", "install", "youtube-dl"])

    elif system == LINUX: #
        #sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
        #sudo chmod a+rx /usr/local/bin/youtube-dl
        subprocess.run([
            "sudo",
            "wget",
            "https://yt-dl.org/downloads/latest/youtube-dl",
            "-O",
            "/usr/local/bin/youtube-dl"
        ])
        subprocess.run([
            "sudo",
            "chmod",
            "a+rx",
            "/usr/local/bin/youtube-dl"
        ])

    else:
        raise OSError("Incompatible System")



def install_youtube_video(link):
    __install_youtube_dl()
    raise NotImplementedError("This function is not implemented yet")

