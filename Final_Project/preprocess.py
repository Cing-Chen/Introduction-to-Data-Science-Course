import pandas as pd

def preprocess():
    train = pd.read_csv('./dataset/train.csv')
    test = pd.read_csv('./dataset/test.csv')

    train_X = train.drop(labels=['label'], axis=1)
    train_Y = train['label']

    return train_X, train_Y, test

# if __name__ == '__main__':
#     preprocess()