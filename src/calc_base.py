# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import sys
from math import radians

def format_df(file, output):
    df = pd.read_csv(file)
    
    # Time-related readings
    
    # Strip leading zero in day (i.e 05 -> 5)
    df["day"] = df["Date"].str.split("/").str.get(0).str.lstrip('0')
    
    # Strip leading zero in month (i.e 05 -> 5)
    df["month"] = df["Date"].str.split("/").str.get(1).str.lstrip('0')
    
    df["year"] = df["Date"].str.split("/").str.get(2)
    
    df["hour"] = df["Time"].str.split(":").str.get(0)
    
    df["minute"] = df["Time"].str.split(":").str.get(1).str.lstrip('0').replace('',0)
    
    df["second"] = df["Time"].str.split(":").str.get(2).str.lstrip('0').replace('',0)
    
    df["delta"] = df["Delta"].shift(periods=-1,fill_value=1)
    
    df["duration"] = df["Duration (Second)"]
    
    # CSS readings
    
    df["css1"] = df["CSS_XP"]/1000
    df["css2"] = df["CSS_XM"]/1000
    df["css3"] = df["CSS_YP"]/1000
    df["css4"] = df["CSS_YM"]/1000
    df["css5"] = df["CSS_ZP"]/1000
    df["css6"] = df["CSS_ZM"]/1000
    
    # Temperature readings
    
    df["t1"] = df["T_X+"] + 273.15
    df["t2"] = df["T_X-"] + 273.15
    df["t3"] = df["T_Y+"] + 273.15
    df["t4"] = df["T_Y-"] + 273.15
    df["t5"] = df["T_Z+"] + 273.15
    df["t6"] = df["T_Z-"] + 273.15
    df["t7"] = df["T_Mid"] + 273.15
    
    df["t1n"] = df["t1"].shift(periods=-1,fill_value=0)
    df["t2n"] = df["t2"].shift(periods=-1,fill_value=0)
    df["t3n"] = df["t3"].shift(periods=-1,fill_value=0)
    df["t4n"] = df["t4"].shift(periods=-1,fill_value=0)
    df["t5n"] = df["t5"].shift(periods=-1,fill_value=0)
    df["t6n"] = df["t6"].shift(periods=-1,fill_value=0)
    df["t7n"] = df["t7"].shift(periods=-1,fill_value=0)
    
    df["dtt1"] = (df["t1n"]-df["t1"])/df["delta"]
    df["dtt2"] = (df["t2n"]-df["t2"])/df["delta"]
    df["dtt3"] = (df["t3n"]-df["t3"])/df["delta"]
    df["dtt4"] = (df["t4n"]-df["t4"])/df["delta"]
    df["dtt5"] = (df["t5n"]-df["t5"])/df["delta"]
    df["dtt6"] = (df["t6n"]-df["t6"])/df["delta"]
    df["dtt7"] = (df["t7n"]-df["t7"])/df["delta"]
    
    # Euler angle
    df["xang"] = df["XAng"].apply(radians)
    df["yang"] = df["YAng"].apply(radians)
    df["zang"] = df["ZAng"].apply(radians)
    
    # Output
    outdf = df[["year","month","day","hour","minute","second",
                "delta","duration",
                "css1","css2","css3","css4","css5","css6",
                "xang","yang","zang",
                "t1","t2","t3","t4","t5","t6","t7",
                "t1n","t2n","t3n","t4n","t5n","t6n","t7n",
                "dtt1","dtt2","dtt3","dtt4","dtt5","dtt6","dtt7"]]
    
    # Drop last row
    outdf = outdf[:-1]
    outdf.to_csv(output,index=False)

def main():
    file = sys.argv[1]
    output = sys.argv[2]
    format_df(file, output)

if __name__ == "__main__":
    main()
