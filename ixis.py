'''
Helper functions for Code Challenge
'''
#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def random_over(data, target, ratio=.5):
    #count size of each target
    count_target_0, count_target_1 = data[target].value_counts()

    #separate data into each target class
    data_0 = data[data[target]==0]
    data_1 = data[data[target]==1]

    data_1_over_sample = data_1.sample(round(count_target_0*ratio), replace=True)

    df_over_sample = pd.concat([data_0,data_1_over_sample], axis=0)

    return df_over_sample

def encode_variables(data, features_to_encode):
    from sklearn.preprocessing import OneHotEncoder

    data_to_encode = data[features_to_encode]

    enc = OneHotEncoder()
    enc = enc.fit(data_to_encode)
    enc_labels = enc.transform(data_to_encode).toarray()

    new_columns=list()

    for col, values in zip(data_to_encode.columns, enc.categories_):
        new_columns.extend([col + '_' + str(value) for value in values])

    new_df= pd.concat([data, pd.DataFrame(enc_labels, columns=new_columns)], axis='columns')
    new_df = new_df.drop(features_to_encode, axis=1)

    return new_df


if __name__ == "__main__":
    print('ixis')
