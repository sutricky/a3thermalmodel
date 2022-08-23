# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
# Create raw plots of node temperature, satellite attitude, and sun sensor from
# base dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, re, math

def main():
    df = pd.read_csv(sys.argv[1])
    date = sys.argv[2]
    nodes = range(1,8)
    for i in range(4):
        # Node temperature plot
        if i < 3:
            plt.figure()
            plt.scatter(df["duration"], df[f"t{2*i+1}"] - 273.15, s = 10)
            plt.scatter(df["duration"], df[f"t{2*i+2}"] - 273.15, s = 10)
            plt.title(f"Suhu Node {2*i+1} dan {2*i+2} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Suhu (°C)")
            plt.legend([f"Node {2*i+1}",f"Node {2*i+2}"])
            plt.savefig(f"fig/raw_node{2*i+1}{2*i+2}_temp_{date}.png", bbox_inches='tight')
            plt.close()
            # Sun sensor plot
            plt.figure()
            plt.scatter(df["duration"], df[f"css{2*i+1}"]*1000, s = 10)
            plt.scatter(df["duration"], df[f"css{2*i+2}"]*1000, s = 10)
            plt.title(f"Arus Sensor Matahari Node {2*i+1} dan {2*i+2} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Arus sensor Matahari (mA)")
            plt.legend([f"Node {2*i+1}",f"Node {2*i+2}"])
            plt.savefig(f"fig/raw_node{2*i+1}{2*i+2}_css_{date}.png", bbox_inches='tight')
            plt.close()
        else:
            plt.figure()
            plt.scatter(df["duration"], df[f"t{2*i+1}"] - 273.15, s = 10)
            plt.title(f"Suhu Node {2*i+1} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Suhu (°C)")
            plt.savefig(f"fig/raw_node{2*i+1}_temp_{date}.png", bbox_inches='tight')
            plt.close()
    
    plt.figure()
    plt.scatter(df["duration"], np.rad2deg(df["xang"]), s = 10)
    plt.scatter(df["duration"], np.rad2deg(df["yang"]), s = 10)
    plt.scatter(df["duration"], np.rad2deg(df["zang"]), s = 10)
    plt.title(f"Sudut Sikap Satelit vs Waktu")
    plt.xlabel("Waktu (s)")
    plt.ylabel("Sudut sikap satelit (°)")
    plt.legend(["Sudut Roll","Sudut Pitch","Sudut Yaw"])
    plt.savefig(f"fig/raw_angle_{date}.png", bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    main()

