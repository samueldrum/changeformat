
from _core._ffmpegvideo import ( 
    __change_format,
    __removetheaudio,
    __change_format_with_high_quality,
    __generate_images_from_video,
    
)


__all__ = [
    "changeformat",
    "removetheaudio",
    "changeformat_WHK"
]

def changeformat(input_file, output_file):

    __change_format(input_file, output_file)



def changeformat_WHK(input_file, output_file):
    """
    change format with high quality
    
    """
    __change_format_with_high_quality(input_file, output_file)



def removetheaudio(input_file, output_file):
    
    __removetheaudio(input_file, output_file)




def gen_images(input_file, output_file, fps=1, exten_imgage="png"):
    __generate_images_from_video(input_file, output_file, fps, exten_imgage)