# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
import sys, re, math

def main():
    df = pd.read_csv(sys.argv[1])
    date = sys.argv[2]
    data = df.sort_values(by=['time'])
    for i in range(4):
        # Temperature plot
        plt.figure()
        if i < 3:
            plt.plot(data["time"], data[f"t{2*i+1}p"]-273.15, data["time"], data[f"t{2*i+1}o"]-273.15, data["time"], data[f"t{2*i+2}p"]-273.15, data["time"], data[f"t{2*i+2}o"]-273.15)
            plt.title(f"Suhu Node {2*i+1} dan {2*i+2} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Suhu (°C)")
            plt.legend([f"Prediksi Node {2*i+1}", f"Observasi Node {2*i+1}",f"Prediksi Node {2*i+2}", f"Observasi Node {2*i+2}"])
            plt.savefig(f"fig/paper_node{2*i+1}{2*i+2}_temp_{date}.png", bbox_inches='tight')
        else:
            plt.plot(data["time"], data[f"t{2*i+1}p"]-273.15, data["time"], data[f"t{2*i+1}o"]-273.15)
            plt.title(f"Suhu Node {2*i+1} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Suhu (°C)")
            plt.legend(['Prediksi', 'Observasi'])
            plt.savefig(f"fig/paper_node{2*i+1}_temp_{date}.png", bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
    main()

