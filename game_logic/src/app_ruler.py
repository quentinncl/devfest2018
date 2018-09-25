# coding: utf-8
from flask import Flask
from flask import request
from flask import jsonify
from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd

app = Flask(__name__)

filename_model = "rnf.model"
with open(filename_model, 'rb') as file:
    model = pickle.load(file)


@app.route("/predict", methods=['GET', 'POST'])
def predict():

    if request.data:
        data = request.get_json()
    else:
        data = request.values
    x = pd.DataFrame(
        {
            'pos_x': [data['pos_x']],
            'pos_y': [data['pos_x']],
            'cell_value': [data['cell_value']],
            'board_size': [data['board_size']],
            'ite': [data['ite']],
        }
    )
    print(x)
    res = model.predict(x)
    print(res)
    return jsonify({'pred':int(res[0])})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
