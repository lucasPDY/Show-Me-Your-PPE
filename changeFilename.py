import os
for fileName in os.listdir():
    if fileName!="changeFilename.py" and fileName!=".DS_Store":

        os.rename(fileName,(fileName[:-4]+ "b.xml"))
