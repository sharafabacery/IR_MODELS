import os
import random
import shutil


class GenrateFile:
    dirName = "Documents"
    arrayWord = ['A', 'B', 'C', 'D', 'E', 'F']
    arrayDocuments = []

    def __init__(self, numofdoc):
        for iterator in range(numofdoc):
            self.arrayDocuments.append("Document" + str(iterator + 1) + ".txt")

    def createdir(self):
        root_dir = os.path.abspath(os.curdir)  # root dir
        path = os.path.join(root_dir, self.dirName)
        flag = True
        try:
            os.mkdir(path)
        except OSError:
            flag = False
        return flag

    def deletedir(self):
        root_dir = os.path.abspath(os.curdir)  # root dir
        path = os.path.join(root_dir, self.dirName)
        flag = True
        try:
            shutil.rmtree(path)
        except OSError:
            flag = False
        return flag

    def genratestring(self, min, max, chars):
        return " ".join("".join(random.choice(str(chars)) for _ in range(random.randint(min, max))))

    def genrateandfill(self, pathfile, string):
        file = open(pathfile, "w")
        file.write(string)
        file.close()

    def mix(self, chars, min, max):
        self.deletedir()
        flag = self.createdir()
        print(flag)
        if flag:
            root_dir = os.path.abspath(os.curdir)
            print(root_dir)
            for Document in self.arrayDocuments:
                try:
                    self.genrateandfill(os.path.join(os.path.join(root_dir, self.dirName), Document),
                                        self.genratestring(min=min, max=max, chars=chars))
                except:
                    return False
            return True
        else:
            return False
