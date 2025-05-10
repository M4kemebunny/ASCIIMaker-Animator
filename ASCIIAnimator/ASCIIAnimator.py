import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
Animname = input("Type a name for animation:")
Fps = float(input("Type fps for the animation:"))
Duration = Fps/100
Ms = float(Duration)
counter = 1
exportedpath = (ROOT_DIR+"\\ExportedAnim\\")
txtpath = (ROOT_DIR+"\\txtASCIIs")
exportedtxt = open((ROOT_DIR+"\\ExportedAnim\\"+Animname+".py"), "a+")
dir_list = os.listdir(txtpath)
for step in dir_list:
    countfiles = len(dir_list)
    
    if counter == 1:
        exporttxt = exportedtxt.write("""import os
import time
from replit import clear

moves = [
"""+'"""'+"""
""")
    if counter == countfiles:
        txt = open(txtpath+"\\"+step)
        readedtxt = txt.read()
        exporttxt = exportedtxt.write(readedtxt+('"""')+"""
    """)
        exporttxt = exportedtxt.write("""
]
while True:
    for step in moves:
        print(step)
        time.sleep(""")
        exporttxt = exportedtxt.write(str(Ms))
        exporttxt = exportedtxt.write(""")
        os.system('cls')""")
        print(counter, "/", countfiles)
        exit()
    txt = open(txtpath+"\\"+step)
    readedtxt = txt.read()
    exporttxt = exportedtxt.write(readedtxt+('""", """')+"""
    """)
    print(counter, "/", countfiles)
    counter += 1