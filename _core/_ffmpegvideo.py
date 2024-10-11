
"""
Change format library only support 3 OS

windows - linux - macos

"""
import subprocess
from _core._ffmpegcfg import install_ffmpeg



def __change_format(input_file, ouput_file):

    # ffmpeg -i input_file.mp4 output_file.mkv

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, ouput_file])


def __change_format_with_high_quality(input_file, ouput_file):

    # ffmpeg -i input_video.mkv -c:v copy output_video.mp4

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, "-c:v", "copy", ouput_file])
    




def __removetheaudio(input_file, output_file):

    # ffmpeg -i input_video.mp4 -an output_video.mp4

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, "-an", output_file])


def __generate_images_from_video(input_file, output_file, fps=1, exten_imgage="png"):

    #ffmpeg -i input_video.mp4 -vf "fps=1" output_%04d.png

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, "-vf", f"fps={fps}", f"{output_file}%04d.{exten_imgage}"])



