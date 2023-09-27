import easygui
from rembg import remove
from PIL import Image

inputpath = easygui.fileopenbox(title="selectimage")
outputpath = easygui.filesavebox(title="saveimage")

input = Image.open(inputpath)
output = remove(input)
output.save(outputpath)