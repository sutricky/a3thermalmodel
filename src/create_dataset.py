# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import sys
import pandas as pd
import numpy as np
from scipy.stats import zscore

def get_outliers(df):
    zdt = np.abs(zscore(df[["dtt1","dtt2","dtt3","dtt4","dtt5","dtt6","dtt7"]].to_numpy())).T
    zt = np.abs(zscore(df[["t1","t2","t3","t4","t5","t6","t7"]].to_numpy())).T
    # Rate of temperature change outlier
    dt_out = np.where(zdt > 3)[1]
    # Temperature outlier
    t_out = np.where(zt > 3)[1]
    # Delta outlier ( time step > 120 s)
    delta_out = np.where(df["delta"] > 120)[0]
    return np.unique(np.sort(np.concatenate((dt_out,t_out,delta_out))))


def main():
    basedf = pd.read_csv(sys.argv[1])
    outliers = get_outliers(basedf)
    solardf = pd.read_csv(sys.argv[2]).drop(outliers)
    albdf = pd.read_csv(sys.argv[3]).drop(outliers)
    earthdf = pd.read_csv(sys.argv[4]).drop(outliers)
    output = sys.argv[5]
    out_df = pd.concat([solardf, albdf, earthdf, basedf.drop(outliers)], axis=1, join='inner')
    out_df.to_csv(output, index=False)

if __name__ == "__main__":
    main()
