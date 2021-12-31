import pandas as pd

# Random Forest Module
# --------------------
from sklearn.metrics import accuracy_score
# --------------------


def evaluate(model, model_selector, data, label):
    accuracy = None

    if model_selector == 'Random_Forest':
        predict = model.predict(data)
        accuracy = accuracy_score(predict, label)
    elif model_selector == 'SVM':
        print(2)
    elif model_selector == 'KNN':
        print(3)
    else:
        print('hello world')
        
    return accuracy


def predict(model, model_selector, data):
    predict = None

    if model_selector == 'Random_Forest':
        predict = model.predict(data)
    elif model_selector == 'SVM':
        print(2)
    elif model_selector == 'KNN':
        print(3)
    else:
        print('hello world')

    output = pd.read_csv("./dataset/sample_submission.csv")
    output['Label'] = predict
    output.to_csv(f"./outputs/output_{model_selector}.csv",index=False)