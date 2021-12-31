def training(X, Y, model, model_selector):
    model = None

    if model_selector == 'random forest':
        model.fit(X, Y)
    elif model_selector == 'SVM':
        print(2)
    elif model_selector == 'KNN':
        print(3)
    else:
        print('hello world')

    return model