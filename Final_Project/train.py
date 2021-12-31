def train(X, Y, model, model_selector):
    if model_selector == 'Random_Forest':
        model.fit(X, Y)
    elif model_selector == 'SVM':
        # Train in this part
        print('hello world')
    elif model_selector == 'KNN':
        # Train in this part
        print('hello world')
    else:
        print('This is impossible case.')

    return model