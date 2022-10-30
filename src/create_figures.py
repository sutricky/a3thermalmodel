# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import sys, re, math

def main():
    df = pd.read_csv(sys.argv[1])
    date = sys.argv[2]
    data = df.sort_values(by=['time'])
    nodes = range(1,8)
    rmse = []
    r2 = []
    mae = []
    abs_error = [[]]
    node_error = [[]]
    for i in range(7):
        abs_error.append((data[f"t{i+1}p"]-data[f"t{i+1}o"]).abs())
        node_error.append((data[f"t{i+1}p"]-data[f"t{i+1}o"]))
        # Temperature plot
        plt.figure()
        plt.plot(data["time"], data[f"t{i+1}p"]-273.15, data["time"], data[f"t{i+1}o"]-273.15)
        plt.title(f"Suhu Node {i+1} vs Waktu")
        plt.xlabel("Waktu (s)")
        plt.ylabel("Suhu (°C)")
        plt.legend(['Prediksi', 'Observasi'])
        plt.savefig(f"fig/node{i+1}_temp_{date}.png", bbox_inches='tight')
        plt.close()
        
        # Individual node error plot
        plt.figure()
        plt.plot(data["time"], (data[f"t{i+1}p"]-data[f"t{i+1}o"]))
        plt.title(f"Error Suhu Node {i+1} vs Waktu")
        plt.xlabel("Waktu (s)")
        plt.ylabel("Error (°C)")
        plt.savefig(f"fig/node{i+1}_node_error_{date}.png", bbox_inches='tight')
        plt.close()
        
        # Absolute node error plot
        plt.figure()
        plt.plot(data["time"], (data[f"t{i+1}p"]-data[f"t{i+1}o"]).abs())
        plt.title(f"Error Suhu Absolut Node {i+1} vs Waktu")
        plt.xlabel("Waktu (s)")
        plt.ylabel("Error (°C)")
        plt.savefig(f"fig/node{i+1}_abs_error_{date}.png", bbox_inches='tight')
        plt.close()
        
        # RMSE plot
        rmse.append(mean_squared_error(data[f"t{i+1}o"]-273.15, data[f"t{i+1}p"]-273.15,squared=False))
        # MAE plot
        mae.append(mean_absolute_error(data[f"t{i+1}o"]-273.15, data[f"t{i+1}p"]-273.15))
        # R2 plot
        r2.append(r2_score(data[f"t{i+1}o"], data[f"t{i+1}p"]))

    plt.figure()
    plt.bar(nodes, rmse)
    plt.yticks(np.arange(0,1.1,step=0.1))
    plt.title("RMSE Node Satelit")
    plt.xlabel("Node")
    plt.ylabel("Error (°C)")
    plt.savefig(f"fig/rmse_{date}.png", bbox_inches='tight')
    plt.close()
    plt.figure()
    plt.bar(nodes, mae)
    plt.title("Mean Absolute Error")
    plt.xlabel("Node")
    plt.ylabel("Error (°C)")
    plt.savefig(f"fig/mae_{date}.png", bbox_inches='tight')
    plt.close()
    plt.figure()
    plt.rcParams.update({'mathtext.default': 'regular' })
    plt.bar(nodes, r2)
    plt.yticks(np.arange(0,1.1,step=0.1))
    plt.title('Skor $R^2$ Node Satelit')
    plt.xlabel("Node")
    plt.ylabel('Skor $R^2$')
    plt.savefig(f"fig/r2_{date}.png", bbox_inches='tight')
    plt.close()
    abs_error = np.array(abs_error[1:])
    node_error = np.array(node_error[1:])
    mean_deviation = np.mean(abs_error, axis=0)
    std_deviation = np.std(abs_error, axis=0, ddof=1)
    plt.figure()
    plt.plot(data["time"], mean_deviation)
    plt.title("Mean Deviation")
    plt.xlabel("Time (s)")
    plt.ylabel("Deviation (°C)")
    plt.savefig(f"fig/mean_deviation_{date}.png", bbox_inches='tight')
    plt.close()
    plt.figure()
    plt.plot(data["time"], std_deviation)
    plt.title("Standard Deviation")
    plt.xlabel("Time (s)")
    plt.ylabel("Deviation (°C)")
    plt.savefig(f"fig/std_deviation_{date}.png", bbox_inches='tight')
    plt.close()
    max_node_error = np.max(node_error, axis=1)
    plt.figure()
    plt.bar(nodes, max_node_error)
    plt.title("Maximum Node Error")
    plt.xlabel("Node")
    plt.ylabel("Error (°C)")
    plt.savefig(f"fig/max_node_error_{date}.png", bbox_inches='tight')
    plt.close()
    max_abs_node_error = np.max(abs_error, axis=1)
    plt.figure()
    plt.bar(nodes, max_abs_node_error)
    plt.title("Maximum Absolute Node Error")
    plt.xlabel("Node")
    plt.ylabel("Error (°C)")
    plt.savefig(f"fig/max_abs_node_error_{date}.png", bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()

