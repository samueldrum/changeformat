
from _core.ffmpegcf import _change_format, _removetheaudio


__all__ = [
    "changeformat",
    "removetheaudio",
]

def changeformat(input_file, output_file):

    _change_format(input_file, output_file)



def removetheaudio(input_file, output_file):
    
    _removetheaudio(input_file, output_file)