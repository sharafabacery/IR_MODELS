import os
import random
import shutil


class GenrateFile:
    dirName = "Documents"
    arrayDocuments = []

    def __init__(self, numOfDoc):
        for iterator in range(numOfDoc):
            self.arrayDocuments.append("Document" + str(iterator + 1) + ".txt")

    def createDir(self):
        root_dir = os.path.abspath(os.curdir)  # root dir
        path = os.path.join(root_dir, self.dirName)
        flag = True
        try:
            os.mkdir(path)
        except OSError:
            flag = False
        return flag

    def deleteDir(self):
        root_dir = os.path.abspath(os.curdir)  # root dir
        path = os.path.join(root_dir, self.dirName)
        flag = True
        try:
            shutil.rmtree(path)
        except OSError:
            flag = False
        return flag

    def genrateString(self, minNumChar, maxNumChar, chars):
        return " ".join("".join(random.choice(str(chars)) for _ in range(random.randint(minNumChar, maxNumChar))))

    def genrateAndFill(self, pathFile, string):
        file = open(pathFile, "w")
        file.write(string)
        file.close()

    def mix(self, chars, minMix, maxMix):
        self.deleteDir()
        flag = self.createDir()
        if flag:
            root_dir = os.path.abspath(os.curdir)
            for Document in self.arrayDocuments:
                self.genrateAndFill(os.path.join(os.path.join(root_dir, self.dirName), Document),
                                    self.genrateString(minNumChar=minMix, maxNumChar=maxMix, chars=chars))
            return True
        else:
            return False
