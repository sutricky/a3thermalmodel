# Configuration file

# Limit for Coarse Sun Sensor threshold.
# CSS readings less than or equal to this value will be considered 0.
# Value is in Ampere
CSSLIMIT = 0.00049

# Radius of the Earth
# Must be in integer
# Value is in km
REARTH = 6371

# Ratio for test:train dataset split. 
# Default value of 0.3 means 30%
# of the dataset will used for testing.
# Value is in float
RATIO = 0.3

# Seed for machine learning random state
# Default value of 0 following Scikit-learn's documentation
# Value must be integer in the range of [0, 2**32 - 1]
SEED = 0
