
import subprocess
import warnings

from OS import LINUX, MACOS, WINDOWS, detect_system





def _check_ffmpeg_installed():
    try:
        result = subprocess.run(["ffmpeg", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return True
    except FileNotFoundError:
        return False
    return False


def install_ffmpeg():
    print("Verifying if ffmpeg is installed")

    if _check_ffmpeg_installed():
        print("ffmpeg is already installed")
        return
    
    else:
        system = detect_system().lower()

        if system == WINDOWS: # Widows
            print("Installing ffmpeg using winget...")
            subprocess.run(["winget", "install", "ffmpeg"],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        elif system == MACOS:  # macOS
            print("Installing ffmpeg using brew...")
            subprocess.run(["brew", "install", "ffmpeg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        elif system == LINUX:  # It's just only for Ubuntu based
            print("Installing ffmpeg using apt...")
            subprocess.run(["sudo", "apt", "install", "ffmpeg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        else:
            raise OSError(f"System '{system}' not compatible")

    warnings.warn("I highly recommend you to restart the IDE or code editor that you are using now", UserWarning)
    
