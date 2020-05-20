import xml.etree.ElementTree as ET
import os

xmlDirectory = "/Users/dennis_teo/Desktop/xmldata/"
# print(os.listdir(xmlDirectory))
# print(os.listdir(xmlDirectory))

for xml in os.listdir(xmlDirectory):
    print(xml,"hashs")
    if xml !=".DS_Store":
    # root = ET.parse("./xml/" + xml)
    # # print(root)
    # # break
    # Open original file
    # with open(xmlDirectory+xml, "w+") as f:
    #     text = f.read().replace("hardhat", "vest")
    #     f.write(text)
        root = ET.parse(xmlDirectory+xml)
        for name in root.iter("filename"):
            name.text = (xml[:-4] + ".jpg")
        root.write(xmlDirectory+xml)
        
    # break
#     root[6][0].text = "vest"

