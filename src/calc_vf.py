# LAPAN-A3 Satellite Thermal Modelling
# Copyright (c) 2022 Ricky Sutardi
import pandas as pd
import numpy as np
import skyfield.api
import sys

def utc_timescale(year, month, day, hour, minute, second):
    return skyfield.api.load.timescale().utc(year, month, day, hour, minute, second)

def sat_position_vector(sat):
    return np.stack((sat.position.km[0], sat.position.km[1], sat.position.km[2]), axis=1)

# View factor calculation
def angle_between(v1, v2):
    v1_u = v1/np.linalg.norm(v1)
    v2_u = v2/np.linalg.norm(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
        
def surface_norm(norm, ang):
    c1 = np.cos(ang[0])
    c2 = np.cos(ang[1])
    c3 = np.cos(ang[2])
    s1 = np.sin(ang[0])
    s2 = np.sin(ang[1])
    s3 = np.sin(ang[2])
    r1 = c2*c1
    r2 = c2*s1
    r3 = -s2
    r4 = s3*s2*c1-c3*s1
    r5 = s3*s2*s1+c3*c1
    r6 = s3*c2
    r7 = c3*s2*c1 + s3*s1
    r8 = c3*s2*s1 - s3*c1
    r9 = c3*c2
    rot = np.array([[r1, r2, r3], [r4, r5, r6], [r7, r8, r9]])
    return np.dot(rot, norm)
        
# View-factor
def get_fip(b, h):
    if b > 0.5*np.pi:
        b = np.pi - b
        if np.fabs(b) <= np.arccos(1/h):
            return np.cos(b)/(h**2)
        else:
            x = np.sqrt(h**2-1)
            y = -x/np.tan(b)
            z1 = (np.cos(b)*np.arccos(y)-x*np.sin(b)*np.sqrt(1-(y**2)))/(np.pi*(h**2))
            z2 = np.arctan(np.sin(b)*np.sqrt(1-(y**2))/x)/np.pi
            return z1 + z2        
    else:
        return 0

def main():
    tle = sys.argv[1]
    basedf = pd.read_csv(sys.argv[2])
    rearth = int(sys.argv[3])
    output = sys.argv[4]

    utc = utc_timescale(basedf['year'].to_numpy(), basedf['month'].to_numpy(), basedf['day'].to_numpy(), basedf['hour'].to_numpy(), basedf['minute'].to_numpy(), basedf['second'].to_numpy())
    
    sat = skyfield.api.load.tle_file(tle)[0].at(utc)
    rsat = sat_position_vector(sat)
    sat_ang = basedf[["xang","yang","zang"]].to_numpy()
    node_angles = np.zeros((6, sat_ang.shape[0]))
    view_factors = np.zeros((6, sat_ang.shape[0]))
    body_norm = np.array([[1, 0, 0],[-1, 0, 0],[0, 1, 0],[0, -1, 0],[0, 0, 1],[0, 0, -1]])
    # For each surface node
    for i in range(6):
        # For each surface node angles
        for j in range(sat_ang.shape[0]):
            node_angles[i][j] = angle_between(rsat[j], surface_norm(body_norm[i], sat_ang[j]))
            view_factors[i][j] = get_fip(node_angles[i][j], np.linalg.norm(rsat[j])/rearth)
    out_df = pd.DataFrame(
        {
            'vf1': view_factors[0],
            'vf2': view_factors[1],
            'vf3': view_factors[2],
            'vf4': view_factors[3],
            'vf5': view_factors[4],
            'vf6': view_factors[5],
        }
    )
    out_df.to_csv(output, index=False)    

if __name__ == "__main__":
    main()
