import os


class StatisticalModel:
    arrayResults = {}
    arrayDocuments = []
    rating = {}
    query = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
             'F': 0}
    path = ""

    def __init__(self):
        self.path = os.path.join(os.path.curdir, "Documents")
        it = len(os.listdir(self.path))
        for iterator in range(it):
            index = "Document" + str(iterator + 1) + ".txt"
            self.arrayResults[index] = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0,
                                        'F': 0}
            self.arrayDocuments.insert(iterator, index)

    def statisticalString(self, filename):
        filtered = open(os.path.join(self.path, filename), 'r')
        content = filtered.read()
        bagofwords = {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'F': 0.0}
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

    def prepareQuery(self, thisquery):
        thisquery = "".join(thisquery.split())
        thisquery = thisquery.upper()
        thisquery = thisquery.replace('QUERY:<', '')
        thisquery = thisquery.replace('>', '')
        thisquery = thisquery.split(";")
        thirstier = {}
        for qq in thisquery:
            thisquery1 = qq.split(":")
            if len(thisquery1) >1:
                thirstier[thisquery1[0]] = float(thisquery1[1])
        thirstier = dict(sorted(thirstier.items(), key=lambda item: item[0]))
        for word in ['A', 'B', 'C', 'D', 'E', 'F']:
            if word in thirstier:
                self.query[word] = float(thirstier[word])
            else:
                self.query[word] = 0
        return self.query
