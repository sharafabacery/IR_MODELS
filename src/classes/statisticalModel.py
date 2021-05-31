import os


class StatisticalModel:
    arrayResults = {}
    arrayDocuments = []
    rating = {}
    charChoosen=""
    query = {}
    path = ""

    def __init__(self,charChoosen):
        self.path = os.path.join(os.path.curdir, "Documents")
        it = len(os.listdir(self.path))
        self.charChoosen=charChoosen
        for iterator in charChoosen:
           self.query[iterator]=0
        for iterator in range(it):
            index = "Document" + str(iterator + 1) + ".txt"
            self.arrayResults[index] = self.query
            self.arrayDocuments.insert(iterator, index)

    def statisticalString(self, filename):
        filtered = open(os.path.join(self.path, filename), 'r')
        content = filtered.read()
        bagofwords = {}
        for iterator in self.charChoosen:
            bagofwords[iterator]=0
        length = len("".join(content.split()))
        for char in content:
            if char != " ":
                bagofwords[char] = bagofwords[char]+(1 / length)
        return bagofwords

    def structureOfModel(self):
        for doc in self.arrayDocuments:
            self.arrayResults[doc] = self.statisticalString(doc)

    def dotProduct(self):
        for key in self.arrayResults:
            score = 0.0
            for hkey in self.arrayResults[key]:
                score += self.arrayResults[key][hkey] * self.query[hkey]
            self.rating[key] = score
        return dict(sorted(self.rating.items(), key=lambda item: item[1], reverse=True))

    def prepareWeightQuery(self, thisquery):
        thisquery = "".join(thisquery.split())
        thisquery = thisquery.upper()
        thisquery = thisquery.replace('QUERY:<', '')
        thisquery = thisquery.replace('>', '')
        thisquery = thisquery.split(";")
        thirstier = {}
        for qq in thisquery:
            thisquery1 = qq.split(":")
            if len(thisquery1) >1:
                if float(thisquery1[1])>=0 and float(thisquery1[1])<1:
                    thirstier[thisquery1[0]] = float(thisquery1[1])
                else:
                    return 0
        thirstier = dict(sorted(thirstier.items(), key=lambda item: item[0]))
        listOfChar=[char for char in self.charChoosen]
        for word in listOfChar:
            if word in thirstier:
                self.query[word] = float(thirstier[word])
            else:
                self.query[word] = 0
        return self.query

    def prepareUnWeightQuery(self,thisquery):
        length = len("".join(thisquery.split()))
        for word in thisquery:
            if word !=" ":
                self.query[word]=self.query[word]+(1 / length)
        return  self.query