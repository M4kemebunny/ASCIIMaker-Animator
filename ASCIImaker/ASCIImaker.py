from ascii_magic import AsciiArt
import os
import time
import replit
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = (ROOT_DIR+"\\Frames\\")
dir_list = os.listdir(path)
os.system('cls')
for step in dir_list:
    my_art = AsciiArt.from_image(ROOT_DIR+'\\Frames\\'+step)
    txtstep = step.replace(".png", "")
    txtstep = step.replace(".jpg", "")
    txtstep = step.replace(".jpeg", "")
    my_art.to_file(('ASCIItxt\\'+txtstep+'.txt'), columns=1024, monochrome=True)
    os.system('cls')