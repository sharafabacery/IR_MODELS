from flask import *
import os

import classes.genrateFiles
import classes.statisticalModel

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generateFilesStatModel', methods=['GET'])
def generateFilesStatModel():
    if request.method == "GET":
        obj = classes.genrateFiles.GenrateFile(10)
        obj.mix("ABCDEF", 100, 250)
        return redirect(url_for('index'))


@app.route('/generateFilesVectorModel', methods=['GET'])
def generateFilesVectorModel():
    if request.method == "GET":
        obj = classes.genrateFiles.GenrateFile(10)
        obj.mix("ABCDEF", 1, 10)
        return redirect(url_for('index'))


@app.route('/statisticalModel', methods=['POST', 'GET'])
def statisticalModelFunc():
    obj1 = classes.statisticalModel.StatisticalModel()
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
    # return redirect(url_for('index'))
    return render_template('results.html', results=results,model="statistical Model")


@app.route('/document/<document>')
def body1(document):
    filtered = open(os.path.join(os.path.join(os.path.curdir, "Documents"), document), 'r')
    print(os.path.join(os.path.join(os.path.curdir, "Documents"), document))
    content = filtered.read()

    return '%s' % content


if __name__ == '__main__':
    app.run()
