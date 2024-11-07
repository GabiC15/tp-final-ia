import ast
import pandas
import numpy as np
from math import sqrt

def get_dataset(filename, size):
    length = int(sqrt(size))
    df = pandas.read_csv(f'datasets/{filename}')
    df['data'] = df['data'].apply(ast.literal_eval)
    df['data'] = df['data'].apply(lambda x: np.array(x))
    df['data'] = df['data'].apply(lambda x: 
                                    x.reshape(length, 200//length, length, 200//length)
                                    .max(axis=(1, 3))
                                    .flatten())
    return df["data"].tolist()
