
from _core.ffmpegcf import _change_format, _removetheaudio, _change_format_with_high_quality


__all__ = [
    "changeformat",
    "removetheaudio",
    "changeformat_WHK"
]

def changeformat(input_file, output_file):

    _change_format(input_file, output_file)


def changeformat_WHK(input_file, output_file):
    """
    change format with high quality
    
    """
    _change_format_with_high_quality(input_file, output_file)



def removetheaudio(input_file, output_file):
    
    _removetheaudio(input_file, output_file)