import os
from flask import Flask, request, render_template
from .crop_rec import CropRec
from .utils import plot_graph

static_url_path = os.path.join(os.getcwd(), 'application/static')
app = Flask(__name__, static_url_path=static_url_path)
rec_model = CropRec()
rec_model.load_model()


@app.route('/', methods=["GET", "POST"])
def hello_world():
    content = None
    if request.method == "POST":
        features = []
        # features.append('post method called')
        features.append(request.form.get('N'))
        features.append(request.form.get('P'))
        features.append(request.form.get('K'))
        features.append(request.form.get('Temperature'))
        features.append(request.form.get('Humidity'))
        features.append(request.form.get('PH'))
        features.append(request.form.get('Rainfall'))
        label, probability = rec_model.predict(features)
        # print(label, probability)
        path = plot_graph(probability)
        # print(path)
        content = {
            "label": label[0],
            "plot_path": path,
            "probability": probability
        }
        return render_template('index.html', content=content)
    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
