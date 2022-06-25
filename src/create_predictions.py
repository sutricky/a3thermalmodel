# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import numpy as np
import sys, re
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    basedf = pd.read_csv(sys.argv[1])
    output = sys.argv[len(sys.argv)-1]
    date = re.search(r"prediction_(.*).csv",sys.argv[len(sys.argv)-1]).group(1)
    seed =  int(sys.argv[len(sys.argv)-2])
    ratio = float(sys.argv[len(sys.argv)-3])
    m = LinearRegression()
    predictions = [[]]
    for i in range(7):
        df = pd.read_csv(sys.argv[i+2])
        y = df.iloc[:,-1]
        if i < 6:
            x = df.iloc[:,0:17]
        else:
            x = df.iloc[:,0:14]
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=ratio, random_state=seed)
        m.fit(xtrain, ytrain)
        p = m.predict(xtest)
        predictions.append(p)
    test_index = np.array(ytest.index)
    time = basedf["duration"][test_index].to_numpy()
    delta = basedf["delta"][test_index].to_numpy()
    temp_obs_start = basedf.columns.get_loc("t1")
    temp_next_start = basedf.columns.get_loc("t1n")
    temp_obs = basedf.iloc[test_index,temp_obs_start:temp_obs_start+7].to_numpy().T
    temp_next = basedf.iloc[test_index,temp_next_start:temp_next_start+7].to_numpy().T
    predictions = np.array(predictions[1:])
    temp_preds = temp_obs + predictions*delta
    out_df = pd.DataFrame(
        {
            'data_index': test_index,
            'time': time,
            't1o': temp_next[0],
            't2o': temp_next[1],
            't3o': temp_next[2],
            't4o': temp_next[3],
            't5o': temp_next[4],
            't6o': temp_next[5],
            't7o': temp_next[6],
            't1p': temp_preds[0],
            't2p': temp_preds[1],
            't3p': temp_preds[2],
            't4p': temp_preds[3],
            't5p': temp_preds[4],
            't6p': temp_preds[5],
            't7p': temp_preds[6],
        })
    out_df.to_csv(output, index=False)

if __name__ == "__main__":
    main()
