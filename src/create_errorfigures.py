# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
# Create plots of node temperature error distribution
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    df = pd.read_csv(sys.argv[1])
    date = sys.argv[2]
    error = []
    for i in range(7):
        # Appends error
        error = np.append(error, (df[f"t{i+1}p"]-df[f"t{i+1}o"]).to_numpy())
    plt.figure()
    plt.hist(error, bins=[-4,-3,-2,-1,0,1,2,3,4])
    plt.title(f"Node Temperature Error Distribution")
    plt.xlabel("Error (°C)")
    plt.ylabel("Frequency")
    plt.savefig(f"fig/error_{date}.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()

