import pickle
import os
import numpy as np


class CropRec(object):

    def __init__(self):
        cwd = os.getcwd()
        self.model_path = os.path.join(cwd, 'model.pkl')
        self.all_labels = ['apple', 'banana', 'blackgram',
                           'chickpea',
                           'coconut',
                           'coffee',
                           'cotton',
                           'grapes',
                           'jute',
                           'kidneybeans',
                           'lentil',
                           'maize',
                           'mango',
                           'mothbeans',
                           'mungbean',
                           'muskmelon',
                           'orange',
                           'papaya',
                           'pigeonpeas',
                           'pomegranate',
                           'rice',
                           'watermelon']

    def load_model(self):
        self.model = None
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)

    def predict(self, data):
        data_pro = []
        for d in data:
            data_pro.append(float(d))
        data = data_pro
        data = np.array(data)
        data = data.reshape(1, -1)
        label = self.model.predict(data)
        probability = self.model.predict_proba(data)
        res = {}
        for i, j in zip(self.all_labels, probability[0]):
            res[i] = j
        return label, res
