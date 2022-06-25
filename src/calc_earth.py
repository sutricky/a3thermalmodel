# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import sys

def main():
    basedf = pd.read_csv(sys.argv[1])
    vfdf = pd.read_csv(sys.argv[2])
    output = sys.argv[3]
    out_df = pd.DataFrame(
        {
            'earth1': vfdf['vf1']*(basedf['t1']**4),
            'earth2': vfdf['vf2']*(basedf['t2']**4),
            'earth3': vfdf['vf3']*(basedf['t3']**4),
            'earth4': vfdf['vf4']*(basedf['t4']**4),
            'earth5': vfdf['vf5']*(basedf['t5']**4),
            'earth6': vfdf['vf6']*(basedf['t6']**4),
        }
    )
    out_df.to_csv(output, index=False)


if __name__ == "__main__":
    main()
