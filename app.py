from flask import Flask, render_template, request, jsonify
import os
import joblib
import numpy as np
import yaml
#from prediction_service import prediction

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

def read_params(config_path=params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    #print(data)
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Some error occured"}
        return error

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                dat = dict(request.form)
                #print(dat)
                a = dat.values()
                b = list(a)
                c = np.array(b)
                d = [list(map(float, c))]
                #print(d)
                respons = predict(d)
                return render_template("index.html", response=respons)
            elif request.json:
                respons = api_response(request)
                return jsonify(respons)

        except Exception as e:
            print(e)
            error = {"error": "Some error occured"}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")


if __name__== "__main__":
    #app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(debug=True)
