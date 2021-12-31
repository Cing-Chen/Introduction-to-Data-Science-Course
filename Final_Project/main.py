# Save models
# --------------------
import joblib
# --------------------

import preprocess as p
import model as m
import train as tr
import test as te

def main():
    train_X, train_Y, valid_X, valid_Y, test = p.preprocess()

    # selectors = ['Random_Forest', 'SVM', 'KNN']
    selectors = ['Random_Forest']
    
    best_accuracy = 0
    best_model = None
    best_model_selector = None

    for selector in selectors:
        model = m.model_select(model_selector=selector)
        model = tr.train(X=train_X, Y=train_Y, model=model, model_selector=selector)
        
        accuracy = te.evaluate(model, selector, valid_X, valid_Y)

        print(f'The accuracy of {selector} model is {accuracy}')
        joblib.dump(model, f'./models/{selector}.model')

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model
            best_model_selector = selector

        te.predict(model, selector, test)

    print(f'The value of the best accuracy is {best_accuracy}')
    print(f'The best model is {best_model_selector}')


if __name__ == '__main__':
    main()