# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
# Create plots of solar heat factor
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys, re, math

def main():
    df = pd.read_csv(sys.argv[1])
    sol = pd.read_csv(sys.argv[2])
    date = sys.argv[3]
    nodes = range(1,7)
    for i in range(3):
            # Solar figures
            plt.figure()
            plt.scatter(df["duration"], sol[f"solar{2*i+1}"], s = 10)
            plt.scatter(df["duration"], sol[f"solar{2*i+2}"], s = 10)
            plt.title(f"Faktor Panas Akibat Matahari Node {2*i+1} dan {2*i+2} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Faktor panas akibat Matahari (A)")
            plt.legend([f"Node {2*i+1}",f"Node {2*i+2}"])
            plt.savefig(f"fig/solar_node{2*i+1}{2*i+2}_{date}.png", bbox_inches='tight')
            plt.close()


if __name__ == "__main__":
    main()

