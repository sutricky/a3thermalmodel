# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
# Create plots of node temperature, satellite attitude, sun sensor, and
# rate of node temperature change from base dataset
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
            plt.scatter(df["duration"], df[f"t{2*i+1}"], s = 10)
            plt.scatter(df["duration"], df[f"t{2*i+2}"], s = 10)
            plt.title(f"Suhu Node {2*i+1} dan {2*i+2} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Suhu (K)")
            plt.legend([f"Node {2*i+1}",f"Node {2*i+2}"])
            plt.savefig(f"fig/base_node{2*i+1}{2*i+2}_temp_{date}.png", bbox_inches='tight')
            plt.close()
            # Sun sensor plot
            plt.figure()
            plt.scatter(df["duration"], df[f"css{2*i+1}"], s = 10)
            plt.scatter(df["duration"], df[f"css{2*i+2}"], s = 10)
            plt.title(f"Arus Sensor Matahari Node {2*i+1} dan {2*i+2} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Arus sensor Matahari (A)")
            plt.legend([f"Node {2*i+1}",f"Node {2*i+2}"])
            plt.savefig(f"fig/base_node{2*i+1}{2*i+2}_css_{date}.png", bbox_inches='tight')
            plt.close()
            # Rate of node temperature change plot
            plt.figure()
            plt.scatter(df["duration"], df[f"dtt{2*i+1}"], s = 10)
            plt.scatter(df["duration"], df[f"dtt{2*i+2}"], s = 10)
            plt.title(f"Laju Perubahan Suhu Node {2*i+1} dan {2*i+2} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Laju perubahan suhu (K/s)")
            plt.legend([f"Node {2*i+1}",f"Node {2*i+2}"])
            plt.savefig(f"fig/base_node{2*i+1}{2*i+2}_tempchange_{date}.png", bbox_inches='tight')
            plt.close()
        else:
            plt.figure()
            plt.scatter(df["duration"], df[f"t{2*i+1}"], s = 10)
            plt.title(f"Suhu Node {2*i+1} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Suhu (K)")
            plt.savefig(f"fig/base_node{2*i+1}_temp_{date}.png", bbox_inches='tight')
            plt.close()
            plt.figure()
            plt.scatter(df["duration"], df[f"dtt{2*i+1}"], s = 10)
            plt.title(f"Laju Perubahan Suhu Node {2*i+1} vs Waktu")
            plt.xlabel("Waktu (s)")
            plt.ylabel("Laju perubahan suhu (K/s)")
            plt.savefig(f"fig/base_node{2*i+1}_tempchange_{date}.png", bbox_inches='tight')
            plt.close()

    for j in nodes:
        plt.figure()
        plt.boxplot(df[f"t{j}"])
        plt.title(f"Boxplot Suhu Node {j} vs Waktu")
        plt.ylabel("Suhu (K)")
        plt.savefig(f"fig/base_node{j}_boxplott_{date}.png", bbox_inches='tight')
        plt.close()
        plt.figure()
        plt.boxplot(df[f"dtt{j}"])
        plt.ylabel("Laju perubahan suhu (K/s)")
        plt.title(f"Boxplot Laju Perubahan Suhu Node {j} vs Waktu")
        plt.savefig(f"fig/base_node{j}_boxplotdtt_{date}.png", bbox_inches='tight')
        plt.close()

    
    plt.figure()
    plt.scatter(df["duration"], df["xang"], s = 10)
    plt.scatter(df["duration"], df["yang"], s = 10)
    plt.scatter(df["duration"], df["zang"], s = 10)
    plt.title(f"Sudut Sikap Satelit vs Waktu")
    plt.xlabel("Waktu (s)")
    plt.ylabel("Sudut sikap satelit (rad)")
    plt.legend(["Sudut Roll","Sudut Pitch","Sudut Yaw"])
    plt.savefig(f"fig/base_angle_{date}.png", bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    main()

