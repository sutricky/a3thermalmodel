# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import sys

# Solar factor calculation

def get_sfe(css, limit):
    # Sensor threshold
    if css > limit:
        return 1
    else:
        return 0

def get_fe(css):
    if css > 0:
        return 1
    else:
        return 0

def main():
    base = pd.read_csv(sys.argv[1])
    limit = float(sys.argv[2])
    output = sys.argv[3]
    nfe = base[["css1","css2","css3","css4","css5","css6"]].applymap(lambda css: get_sfe(css, limit))
    solar = base[["css1","css2","css3","css4","css5","css6"]]*nfe
    fe = solar.sum(axis=1).apply(get_fe)
    out_df = pd.DataFrame(
        {
            'solar1': solar['css1'],
            'solar2': solar['css2'],
            'solar3': solar['css3'],
            'solar4': solar['css4'],
            'solar5': solar['css5'],
            'solar6': solar['css6'],
            'fe': fe
        }
    )
    out_df.to_csv(output, index=False)

if __name__ == "__main__":
    main()
