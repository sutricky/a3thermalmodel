# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import numpy as np
import skyfield.api
from skyfield.elementslib import osculating_elements_of
import sys

def utc_timescale(year, month, day, hour, minute, second):
    return skyfield.api.load.timescale().utc(year, month, day, hour, minute, second)

def get_eclipse_start(fe, tar):
    es = []
    it = np.nditer(fe, flags=['c_index'])
    for x in it:
        if x > 0:
            continue
        else:
            if it.index == 0:
                if fe[it.index + 1] == 0:
                    es.append(tar[it.index])
            elif it.index == (fe.size - 1):
                if fe[it.index - 1] > 0:
                    es.append(tar[it.index])
            else:
                if (fe[it.index - 1] > 0 and fe[it.index + 1] == 0):
                    es.append(tar[it.index])
    return es

def get_eclipse_end(fe, tar):
    ee = []
    it = np.nditer(fe, flags=['c_index'])
    for x in it:
        if x > 0:
            continue
        else:
            if it.index == 0:
                if fe[it.index + 1] > 0:
                    ee.append(tar[it.index])
            elif it.index == (fe.size - 1):
                if fe[it.index - 1] == 0:
                    ee.append(tar[it.index])
            else:
                if (fe[it.index - 1] == 0 and fe[it.index + 1] > 0):
                    ee.append(tar[it.index])
    return ee

def get_ga(tar, tar_ssp, tar_es, tar_ee):
    ga = []
    for x in tar:
        if tar_es <= x <= tar_ee:
            ga.append(0)
        else:
            phi_es = tar_es - tar_ssp
            phi = x - tar_ssp
            if x > tar_ee:
                phi = phi - 2*np.pi
            ga.append((((1+np.cos(phi))/2)**2)*(1-((phi/phi_es)**2)))
    return ga


def main():
    tle = sys.argv[1]
    basedf = pd.read_csv(sys.argv[2])
    vfdf = pd.read_csv(sys.argv[3])
    solardf = pd.read_csv(sys.argv[4])
    output = sys.argv[5]

    utc = utc_timescale(basedf['year'].to_numpy(), basedf['month'].to_numpy(), basedf['day'].to_numpy(), basedf['hour'].to_numpy(), basedf['minute'].to_numpy(), basedf['second'].to_numpy())
    sat = skyfield.api.load.tle_file(tle)[0].at(utc)
    tar = osculating_elements_of(sat).true_anomaly.radians
    es_angles = get_eclipse_start(solardf['fe'].to_numpy(), tar)
    ee_angles = get_eclipse_end(solardf['fe'].to_numpy(), tar)
    tar_es = np.min(es_angles)
    tar_ee = np.max(ee_angles)
    eclipse_angle = tar_ee - tar_es
    sunlit_angle = 2*np.pi - eclipse_angle
    phi_es = 0.5*sunlit_angle

    tar_ssp = tar_es - phi_es
    ga = get_ga(tar, tar_ssp, tar_es, tar_ee)

    out_df = pd.DataFrame(
        {
            'alb1': vfdf['vf1']*ga*solardf['fe'],
            'alb2': vfdf['vf2']*ga*solardf['fe'],
            'alb3': vfdf['vf3']*ga*solardf['fe'],
            'alb4': vfdf['vf4']*ga*solardf['fe'],
            'alb5': vfdf['vf5']*ga*solardf['fe'],
            'alb6': vfdf['vf6']*ga*solardf['fe'],
        }
    )
    out_df.to_csv(output, index=False)

if __name__ == "__main__":
    main()
