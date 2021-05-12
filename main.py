from flask import *
import os

import src.classes.genrateFiles
import src.classes.statisticalModel
import src.classes.vectorSpaceModel

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generateFilesStatModel', methods=['GET'])
def generateFilesStatModel():
    if request.method == "GET":
        obj = src.classes.genrateFiles.GenrateFile(10)
        obj.mix("ABCDEF", 100, 250)
        return redirect(url_for('index'))


@app.route('/generateFilesVectorModel', methods=['GET'])
def generateFilesVectorModel():
    if request.method == "GET":
        obj = src.classes.genrateFiles.GenrateFile(10)
        obj.mix("ABCDEF", 1, 10)
        return redirect(url_for('index'))


@app.route('/statisticalModel', methods=['POST', 'GET'])
def statisticalModelFunc():
    obj1 = src.classes.statisticalModel.StatisticalModel()
    if request.method == "POST":
        query = request.form['search']
        IsWeighted = request.form['weight']
    else:
        query = request.args.get['search']
    if IsWeighted == "True":
        obj1.prepareWeightQuery(query)
    else:
        obj1.prepareUnWeightQuery(query)
    obj1.structureOfModel()
    results = obj1.dotProduct()
    return render_template('results.html', results=results, model="statistical Model")


@app.route('/vectorSpaceModel', methods=['POST', 'GET'])
def vectorSpaceModel():
    obj1 = src.classes.vectorSpaceModel.VectorSpaceModel()
    obj1.tfDocuments()
    obj1.idfCalculation()
    obj1.weightCalculation()
    if request.method == "POST":
        query = request.form['search']
    else:
        query = request.args.get['search']
    obj1.querySet(query)

    results = obj1.cosineSimilarity()
    return render_template('results.html', results=results, model="vector-space Model")


@app.route('/document/<document>')
def showContentOfDocument(document):
    filtered = open(os.path.join(os.path.join(os.path.curdir, "Documents"), document), 'r')
    content = filtered.read()
    return '%s' % content


if __name__ == '__main__':
    app.run()
