

from _core._ffmpegaudio import _change_format, _keeptheaudio



__all__ = ["changeformat",
           "keeptheaudio",
        ]


def changeformat(input_file, output_file):
    _change_format(input_file, output_file)





def keeptheaudio(input_file, output_file):
    """
    extract the audio in the video

    """
    _keeptheaudio(input_file, output_file)
