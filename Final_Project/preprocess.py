import pandas as pd

# Split data
# --------------------
from sklearn.model_selection import train_test_split
# --------------------


def preprocess():
    train = pd.read_csv('./dataset/train.csv')
    test = pd.read_csv('./dataset/test.csv')

    train, valid = train_test_split(train, random_state=0, train_size=0.7)

    train_X = train.drop(labels=['label'], axis=1)
    train_Y = train['label']
    valid_X = valid.drop(labels=['label'], axis=1)
    valid_Y = valid['label']

    return train_X, train_Y, valid_X, valid_Y, test

# if __name__ == '__main__':
#     preprocess()