def train(X, Y, model, model_selector):
    if model_selector == 'Random_Forest':
        model.fit(X, Y)
    elif model_selector == 'SVM':
        print(2)
    elif model_selector == 'KNN':
        print(3)
    else:
        print('hello world')

    return model