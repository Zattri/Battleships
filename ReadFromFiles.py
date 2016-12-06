filePath = "C:\\Users\\Zattri\\Desktop\\"

def createFile(name):
    fileName = name + ".txt"

    file = open(filePath + fileName, "w")
    file.write("Let's get down to business...")
    file.write("To defeat the Hun!")
    file.close()


def readFile(name):
    file = open(filePath + name + ".txt", "r")
    line = file.readline()
    while (line != ""):
        print(line + "\n")
        line = file.readline()

createFile("Test")
readFile("Test")
