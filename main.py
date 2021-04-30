from flask import *
import os

import classes.genrateFiles
import classes.statisticalModel

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/genrateFiles', methods=['GET'])
def genrateFiles():
    if request.method == "GET":
        obj = classes.genrateFiles.GenrateFile(10)
        obj.mix("ABCDEF", 100, 250)
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
    return render_template('statisticalmodelresults.html', results=results)


@app.route('/document/<document>')
def body1(document):
    filtered = open(os.path.join(os.path.join(os.path.curdir, "Documents"), document), 'r')
    print(os.path.join(os.path.join(os.path.curdir, "Documents"), document))
    content = filtered.read()

    return '%s' % content


if __name__ == '__main__':
    app.run()

    # obj = classes.genrateFiles.GenrateFile(100)
    # obj.mix("ABCDEF")
    # obj1 = classes.statisticalModel.StatisticalModel()
    # obj1.prepareQuery('Query:  <A:0.8; B:0.5; D:0.8 ;C:0.7>')
    # obj1.structureOfModel()
    # print(obj1.dotProduct())
