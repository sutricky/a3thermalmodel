# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
# Create plots for ICARES presentation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
import sys

def main():
    nodes = range(1,8)
    df1 = pd.read_csv(sys.argv[1])
    df2 = pd.read_csv(sys.argv[2])
    data1 = df1.sort_values(by=['time'])
    data2 = df2.sort_values(by=['time'])
    error1 = []
    error2 = []
    abs_error1 = [[]]
    abs_error2 = [[]]
    rmse_1 = []
    r2_1 = []
    rmse_2 = []
    r2_2 = []
    for i in range(7):
        # Appends error
        error1 = np.append(error1, (df1[f"t{i+1}p"]-df1[f"t{i+1}o"]).to_numpy())
        error2 = np.append(error2, (df2[f"t{i+1}p"]-df2[f"t{i+1}o"]).to_numpy())
        abs_error1.append((data1[f"t{i+1}p"]-data1[f"t{i+1}o"]).abs())
        abs_error2.append((data2[f"t{i+1}p"]-data2[f"t{i+1}o"]).abs())
        rmse_1.append(mean_squared_error(data1[f"t{i+1}o"]-273.15, data1[f"t{i+1}p"]-273.15,squared=False))
        r2_1.append(r2_score(data1[f"t{i+1}o"], data1[f"t{i+1}p"]))
        rmse_2.append(mean_squared_error(data2[f"t{i+1}o"]-273.15, data2[f"t{i+1}p"]-273.15,squared=False))
        r2_2.append(r2_score(data2[f"t{i+1}o"], data2[f"t{i+1}p"]))
    plt.figure()
    plt.hist(error1, bins=[-4,-3,-2,-1,0,1,2,3,4])
    plt.hist(error2, bins=[-4,-3,-2,-1,0,1,2,3,4])
    plt.legend(["19 May 2018","20 May 2018"])
    plt.title(f"Node Temperature Error Distribution")
    plt.xlabel("Error (°C)")
    plt.ylabel("Frequency")
    plt.savefig(f"fig/icares_error_distribution.png", bbox_inches='tight')
    plt.close()

    # Deviation
    abs_error1 = np.array(abs_error1[1:])
    abs_error2 = np.array(abs_error2[1:])
    mean_deviation1 = np.mean(abs_error1, axis=0)
    std_deviation1 = np.std(abs_error1, axis=0, ddof=1)
    mean_deviation2 = np.mean(abs_error2, axis=0)
    std_deviation2 = np.std(abs_error2, axis=0, ddof=1)

    # 19 May

    plt.figure()
    plt.plot(data1["time"], mean_deviation1, data1["time"], std_deviation1)
    plt.title("19 May 2018 Node Temperature Error Deviation")
    plt.xlabel("Time (s)")
    plt.ylabel("Deviation (°C)")
    plt.legend(["Mean Deviation","Standard Deviation"])
    plt.savefig(f"fig/icares_deviation_2022-05-19.png", bbox_inches='tight')
    plt.close()

    # 20 May
    plt.figure()
    plt.plot(data2["time"], mean_deviation2, data2["time"], std_deviation2)
    plt.title("20 May 2018 Node Temperature Error Deviation")
    plt.xlabel("Time (s)")
    plt.ylabel("Deviation (°C)")
    plt.legend(["Mean Deviation","Standard Deviation"])
    plt.savefig(f"fig/icares_deviation_2022-05-20.png", bbox_inches='tight')
    plt.close()

    # RMSE
    plt.figure()
    plt.bar(nodes, rmse_1)
    plt.bar(nodes, rmse_2)
    plt.yticks(np.arange(0,1.1,step=0.1))
    plt.title("Satellite Node RMSE")
    plt.xlabel("Node")
    plt.ylabel("Error (°C)")
    plt.legend(["19 May 2018","20 May 2018"])
    plt.savefig(f"fig/icares_rmse.png", bbox_inches='tight')
    plt.close()
    plt.figure()

    # R2
    plt.figure()
    plt.rcParams.update({'mathtext.default': 'regular' })
    plt.bar(nodes, r2_1)
    plt.bar(nodes, r2_2)
    plt.legend(["19 May 2018","20 May 2018"])
    plt.yticks(np.arange(0,1.1,step=0.1))
    plt.title('Satellite Node $R^2$ Score')
    plt.xlabel("Node")
    plt.ylabel('$R^2$ Score')
    plt.savefig(f"fig/icares_r2.png", bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    main()

