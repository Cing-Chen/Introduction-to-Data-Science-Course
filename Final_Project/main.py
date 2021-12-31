from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import accuracy_score

import preprocess as P
import model as M
import train as T

def main():
    train_X, train_Y, test = P.preprocess()

    names = ['random forest', 'SVM', 'KNN']
    
    for name in names:
        model = M.model_selecting(model_selector=name)
        model = T.training(model=model, model_selector=name)

    
    # predict = randomforest.predict(X_valid)
    # print(str(accuracy_score(predict, Y_valid)))


if __name__ == '__main__':
    main()