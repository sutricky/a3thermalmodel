# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import sys

def main():
    df = pd.read_csv(sys.argv[1])
    date = sys.argv[2]
    temp_start = df.columns.get_loc("t1")
    sol_start = df.columns.get_loc("solar1")
    alb_start = df.columns.get_loc("alb1")
    earth_start = df.columns.get_loc("earth1")
    dtt_start = df.columns.get_loc("dtt1")
    temps = df.iloc[:,temp_start:temp_start+7]
    temps4 = df.iloc[:,temp_start:temp_start+7]**4
    labels = ["sol","alb","earth",
              "t1","t2","t3","t4","t5","t6","t7",
              "t1_4","t2_4","t3_4","t4_4","t5_4","t6_4","t7_4",
              "dtt"]
    for i in range(7):
        dtt = df.iloc[:,dtt_start+i]
        if i < 6:
            sol = df.iloc[:,sol_start+i]
            alb = df.iloc[:,alb_start+i]
            earth = df.iloc[:,earth_start+i]
            out_df = pd.concat([sol, alb, earth, temps, temps4, dtt], axis=1, join='inner').set_axis(labels, axis='columns')
        else:
            out_df = pd.concat([temps, temps4, dtt], axis=1, join='inner').set_axis(labels[3:], axis='columns')
        filename = f"out/n{i+1}_{date}.csv"
        out_df.to_csv(filename, index=False)

if __name__ == "__main__":
    main()
