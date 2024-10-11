from _core._ffmpegcfg import install_ffmpeg
import subprocess



def _keeptheaudio(input_file, output_file):
    

    # ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.mp3

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, "-q:a", "0", "-map", "a", output_file])
    

def _change_format(input_file, ouput_file):

    # ffmpeg -i input_file.mp4 output_file.mkv

    install_ffmpeg()

    subprocess.run(["ffmpeg", "-i", input_file, ouput_file])