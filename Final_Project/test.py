import pandas as pd

# Calculate accuracy
# --------------------
from sklearn.metrics import accuracy_score
# --------------------


def evaluate(model, model_selector, data, label):
    accuracy = None

    if model_selector == 'Random_Forest':
        predict = model.predict(data)
        accuracy = accuracy_score(predict, label)
    elif model_selector == 'SVM':
        # do predict and calculate acc there
        print('hello world')
    elif model_selector == 'KNN':
        # do predict and calculate acc there
        print('hello world')
    else:
        print('This is impossible case.')
        
    return accuracy


def predict(model, model_selector, data):
    predict = None

    if model_selector == 'Random_Forest':
        predict = model.predict(data)
    elif model_selector == 'SVM':
        # do predict
        print('hello world')
    elif model_selector == 'KNN':
        # do predict
        print('hello world')
    else:
        print('This is impossible case.')

    output = pd.read_csv("./dataset/sample_submission.csv")
    output['Label'] = predict
    output.to_csv(f"./outputs/output_{model_selector}.csv",index=False)