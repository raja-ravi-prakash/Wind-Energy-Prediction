from sklearn import linear_model
from flask import Flask, render_template, url_for, request
import numpy as np
import os

# model
data = open('./data/data.csv')

features = []
labels = []
for row in data:
    row = row.split(',')
    del row[0]

    out = []
    for i in row:
        out.append(float(i))
    labels.append(out[0])
    features.append(out[1:])

clf = linear_model.LinearRegression()
clf.fit(np.array(features), np.array(labels))

# model


app = Flask(__name__, static_folder="static")
port = int(os.getenv('PORT', 8000))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/model', methods=['POST', 'GET'])
def model():
    data = request.get_json()['fields']
    result = clf.predict(np.array([data]))
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
