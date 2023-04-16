import json
import pickle
import numpy as np

__data_columns = None
__model = None


def get_churn_proba(*args):
    result = list( __model.predict_proba([[*args]])[0])
    return result


def load_saved_artifacts():
    print('loading saved artifacts..start')
    global __data_columns
    
    with open("./artifacts/columns.json", 'r') as f:
      __data_columns = json.load(f)['data_columns']
    
    global __model
    with open("./artifacts/credit_card_churn.pickle", 'rb') as f:
      __model = pickle.load(f)

    print("loading saved artifacts..done!")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_churn_proba(9,9,9,9,9,9,9))
