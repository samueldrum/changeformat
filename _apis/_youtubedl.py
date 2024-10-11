
from OS import LINUX, MACOS, WINDOWS, detect_system, platform
import subprocess
from enum import Enum


YOUTUBE_DL = "youtube-dl"

#FORMATS

# youtube-dl -f FORMAT_CODE VIDEO_URL

#-------------Audio Only----------------#
class AudioOnly(Enum):
    WEBM55K = 249  # audio only
    WEBM70K = 250  # audio only
    WEBM139K = 251  # audio only
    M4A = 140  # audio only
    OPUS48K = 252  # audio only - Opus codec 48 kbps
    OPUS96K = 253  # audio only - Opus codec 96 kbps
    OPUS160K = 254  # audio only - Opus codec 160 kbps
    MP3 = 141

#-------------Video----------------#
class Video(Enum):
    MP4144P = 160  # video only
    MP4240P = 133  # video only
    MP4360P = 134  # video only
    MP4480P = 135  # video only
    MP4720P = 136  # video only
    MP41080P = 137  # video only
    WEBM360P = 243  # video only
    WEBM480P = 244  # video only
    WEBM720P = 247  # video only
    WEBM1080P = 248  # video only





# Not supported on windows
if detect_system().lower() == WINDOWS:
    raise OSError(f"{platform()} is not compatible with youtubedl api, try WSL")



def __install_youtube_dl():
    system = detect_system().lower()
    if system == WINDOWS:
        print("You might download youtubedl dependency in the official web site")

    elif system == MACOS:
        # brew install youtube-dl
        subprocess. run(["brew", "install", YOUTUBE_DL])

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

    # youtube-dl https://www.youtube.com/watch?v=VIDEO_ID

    subprocess.run([
        YOUTUBE_DL,
        link

    ])

def install_youtube_video_with_path(url, path):
    # youtube-dl -o "meu_video.mp4" https://www.youtube.com/watch?v=VIDEO_ID

    __install_youtube_dl()

    subprocess.run([
        YOUTUBE_DL,
        "-o",
        path,
        url
    ])


def install_media_format(url, format):

    # youtube-dl -f FORMAT_CODE URL_DO_VIDEO

    __install_youtube_dl()

    subprocess([
        YOUTUBE_DL,
        "-f",
        format,
        url
    ])

