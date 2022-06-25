# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import numpy as np
import sys, math
from contextlib import redirect_stdout
from sklearn.metrics import r2_score, mean_squared_error

def main():
    df = pd.read_csv(sys.argv[1])
    data = df.sort_values(by=['time'])
    output = sys.argv[2]
    with open(output, 'w') as f:
        with redirect_stdout(f):
            abs_error = [[]]
            for i in range(7):
                abs_error.append((data[f"t{i+1}p"]-data[f"t{i+1}o"]).abs())
                print(f"node{i+1}_R2",r2_score(data[f"t{i+1}o"], data[f"t{i+1}p"]))
            for i in range(7):
                print(f"node{i+1}_RMSE",math.sqrt(mean_squared_error(data[f"t{i+1}o"]-273.15, data[f"t{i+1}p"]-273.15)))
            abs_error = np.array(abs_error[1:])
            mean_deviation = np.mean(abs_error, axis=0)
            std_deviation = np.std(abs_error, axis=0, ddof=1)
            max_abs_error = np.max(abs_error, axis=1)
            print("MaxMeanDeviation",np.max(mean_deviation))
            print("MaxStandardDeviation",np.max(std_deviation))
            print("MaxNodeError",np.max(max_abs_error))


if __name__ == "__main__":
    main()
