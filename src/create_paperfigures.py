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
            plt.title(f"Node {2*i+1} and {2*i+2} Temperature vs Time")
            plt.xlabel("Time (s)")
            plt.ylabel("Temperature (°C)")
            plt.legend([f"Node {2*i+1} Predicted", f"Node {2*i+1} Observed",f"Node {2*i+2} Predicted", f"Node {2*i+2} Observed"])
            plt.savefig(f"fig/paper_node{2*i+1}{2*i+2}_temp_{date}.png", bbox_inches='tight')
        else:
            plt.plot(data["time"], data[f"t{2*i+1}p"]-273.15, data["time"], data[f"t{2*i+1}o"]-273.15)
            plt.title(f"Node {2*i+1} Temperature vs Time")
            plt.xlabel("Time (s)")
            plt.ylabel("Temperature (°C)")
            plt.legend(['Predicted', 'Observed'])
            plt.savefig(f"fig/paper_node{2*i+1}_temp_{date}.png", bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
    main()

