import os
import math


class VectorSpaceModel:
    documents = {}
    idf = {}
    weight = {}
    query = {}
    similarities = {}
    path = ""
    charChoosen = ""

    def __init__(self, charChoosen):
        self.path = os.path.join(os.path.curdir, 'Documents')
        it = len(os.listdir(self.path))
        self.charChoosen = charChoosen
        for iterator in charChoosen:
            self.query[iterator] = 0
            self.idf[iterator] = 0
        for iterator in range(it):
            index = "Document" + str(iterator + 1) + ".txt"
            self.documents[index] = {char: 0 for char in self.charChoosen}
            self.weight[index] = {char: 0 for char in self.charChoosen}

            self.similarities[index] = 0

    def tfCalc(self, content):
        bagofwords = {char: 0 for char in self.charChoosen}
        for char in content:
            if char != " ":
                bagofwords[char] = bagofwords[char] + 1
        maxvalue = max(bagofwords.values())
        for char in bagofwords:
            bagofwords[char] = bagofwords[char] / maxvalue

        return bagofwords

    def tfPerDocument(self, filename):
        filtered = open(os.path.join(self.path, filename), 'r')
        content = filtered.read()
        calc = self.tfCalc(content.upper())
        return calc

    def tfDocuments(self):
        for doc in self.documents:
            self.documents[doc] = self.tfPerDocument(doc)

    def idfCalculation(self):
        for doc in self.documents:
            for char in self.documents[doc]:
                if self.documents[doc][char] > 0:
                    self.idf[char] = self.idf[char] + 1
        for udiff in self.idf:
            if self.idf[udiff] > 0:
                self.idf[udiff] = math.log(float(self.idf[udiff]), 2)

    def weightCalculation(self):
        for doc in self.documents:
            self.weight[doc] = {index: self.documents[doc][index] * self.idf[index] for index in self.documents[doc]}

    def querySet(self, thisQuery):
        tfQuery = self.tfCalc(thisQuery)
        self.query = {index: tfQuery[index] * self.idf[index] for index in self.idf}

    def cosineSimilarityCalculations(self, weight, query):
        return sum(weight[index] * query[index] for index in weight) / math.sqrt(
            sum(weight[index] * weight[index] for index in weight) * sum(
                query[index] * query[index] for index in query))

    def cosineSimilarity(self):
        for doc in self.documents:
            self.similarities[doc] = self.cosineSimilarityCalculations(self.weight[doc], self.query)
        return dict(sorted(self.similarities.items(), key=lambda item: item[1], reverse=True))
