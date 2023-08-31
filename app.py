from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    clf = pickle.load(open('model.obj', 'rb'))
    print(clf)
    args = request.args
    t = [args['sl'], args['sw'], args['pl'], args['pw']]
    p = clf.predict([t])[0]
    if p == 1:
        return jsonify({"result":"Iris-setosa"})
    elif p == 2:
        return jsonify({"result":"Iris-versicolor"})
    elif p == 3:
        return jsonify({"result":"Iris-virginica"})
    