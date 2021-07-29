
import yaml
import os
import json
import joblib
import numpy as np

params_path = "params.yaml"
schema_path = os.path.join("prediction_service","schema_in.json")


class NotInRange(Exception):
    def __init__(self,message="Values entered are not in range"):
        self.message = message
        super().__init__(self.message)


class NotInCols(Exception):
    def __init__(self,message="Not in columns"):
        self.message = message
        super().__init__(self.message)


def read_params(config_path=params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    print(data)
    prediction = model.predict(data)
    pred = prediction[0]
    print(pred)
    #return prediction[0]
    try:
        if 3 <= pred <= 8:
            return pred
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected results"


def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema


def validate_input(dict_request):
    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCols

    def _validate_values(col, val):
        schema = get_schema()
        #print(np.array(dict_request[col]))

        if not (schema[col]["min"] <= float(np.array(dict_request[col])) <= schema[col]["max"]):
            raise NotInRange

    for col, val in dict_request.items():
        _validate_cols(col)
        _validate_values(col, val)
    return True


def form_response(dict_request):
    if validate_input(dict_request):
        a = dict_request.values()
        b = list(a)
        c = np.array(b)
        print(c)
        d = [list(map(float, c))]
        response = predict(d)

        return response


def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.values())])
            response = predict(data)
            response = {"response": response}
            return response
    except Exception as e:
        response = {"the expected_range": get_schema(), "response": str(e)}
        #print(e)
        #error = {"error": "Some error occured"}
        return response