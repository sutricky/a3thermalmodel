# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, re, math

def main():
    df = pd.read_csv(sys.argv[1])
    date = sys.argv[2]
    xang = df["XAng"]
    yang = df["YAng"]
    zang = df["ZAng"]
    time = df["Duration (Second)"]
    plt.figure()
    plt.plot(time, xang, time, yang, time, zang)
    plt.title(f"Sudut Euler Satelit vs Waktu")
    plt.xlabel("Time (s)")
    plt.ylabel("Sudut Euler (°)")
    plt.legend(['Sudut Roll', 'Sudut Pitch','Sudut Yaw'])
    plt.savefig(f"fig/attitude_{date}.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()

