import os
# Global file path - Change as needed
filePath = "/users/Zattri/Desktop/"

def closeFile(fileVar):
    if (fileVar != None):
        fileVar.close()
    else:
        print("File is not open or does not exist")

def printFile(filePath, fileName):
    fileVar = open(filePath + fileName, "r")
    print(fileVar.read())

def appendItem(filePath, fileName, newItem):
    fileVar = open(filePath + fileName, "a")
    fileVar.write(newItem+"\n")

def createFile(filePath, fileName, fileTitle = None):
    if (os.path.isfile("./" + fileName) == False):
        fileVar = open(filePath + fileName, "x")
        if (fileTitle != None):
            fileVar.write(fileTitle + "\n")
        return fileVar
    else:
        print("File with that name already exists")

def main():
    #fileVar = open(filePath + fileName, "r")
    # Open parameters
    # r - read
    # w - write
    # x - create and write
    # a - append
    # r+ - read and write
    #print(fileVar.read())

    myFile = createFile(filePath, "iloveyou.txt")
    closeFile(myFile)
    appendItem(filePath, "iloveyou.txt", "Hey there sexy")
    closeFile(myFile)
    printFile(filePath, "iloveyou.txt")
    closeFile(myFile)

main()
