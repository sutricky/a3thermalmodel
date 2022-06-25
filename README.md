# Semi-empirical Thermal Modelling of LAPAN-A3 Satellite Using Machine Learning Method

## Notes

This project is based on a 7-nodes model of the LAPAN-A3
microsatellite which consists of 6 nodes for each of the satellite's
sides and 1 node for the satellite's inner structure. It's also assumed that the input data will be categorized by date such that each file represent the satellite's data for the particular day only.

## Configuration

Configuration variables can be set in the config.mk file. Refer to the file for
additional explanation on the available parameters.

## Input

The model needs 2 files for each date, the satellite's TLE and operational
data. The default structure of the files can be seen in the provided input
examples.

## Output

There are 3 main outputs of the satellite thermal model :

1. Temperature predictions of the satellite's nodes
2. Statistics related to the temperature predictions
3. Figures related to the statistics of the temperature predictions

## Instruction

This project requires Python 3.10, pipenv, and GNU Make. After cloning the
project repository, use `make setup` to quicky install required packages. Then,
just run `make` at the project root.

