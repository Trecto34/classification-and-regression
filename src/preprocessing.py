# Preprocessing Data
import numpy as np
from sklearn import preprocessing

# Sample data
input_data = np.array(
    [[5.1, -2.9, 3.3], [-1.2, 7.8, -6.1], [3.9, 0.4, 2.1], [7.3, -9.9, -4.5]]
)

# Binarization
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
"""print(f"\nBinarized data:\n{data_binarized}")

output:  
Binarized data:
[[1. 0. 1.]
 [0. 1. 0.]
 [1. 0. 0.]
 [1. 0. 0.]]

All the values above 2.1 become 1, the remaining values become 0
"""

# Mean Removal
# Before
"""
print(
    f"\nBefore:\nMean = {input_data.mean(axis=0)}\nStd deviation = {input_data.std(axis=0)}"
)

output: 
Before:
Mean = [ 3.775 -1.15  -1.3  ]
Std deviation = [3.12039661 6.36651396 4.0620192 ]
"""

# Remove mean
# After
data_scaled = preprocessing.scale(input_data)
"""
print(
    f"\nAFTER:\nMean = {data_scaled.mean(axis=0)}\nStd deviation = {data_scaled.std(axis=0)}"
)

output:
AFTER:
Mean = [1.11022302e-16 0.00000000e+00 2.77555756e-17]
Std deviation = [1. 1. 1.]
"""

# Scaling
# Min max scaling

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
"""
print(f"Min max scaled data:\n{data_scaled_minmax}")

output:
Min max scaled data:
[[0.74117647 0.39548023 1.        ]
 [0.         1.         0.        ]
 [0.6        0.5819209  0.87234043]
 [1.         0.         0.17021277]]
"""

# Normalization
# Normalize data
data_normalized_L1 = preprocessing.normalize(input_data, norm="l1")
data_normalized_L2 = preprocessing.normalize(input_data, norm="l2")
"""
print(
    f"L1 normalized data:\n{data_normalized_L1}\n\nL2 normalized data:\n{data_normalized_L2}"
)

output:

L1 normalized data:
[[ 0.45132743 -0.25663717  0.2920354 ]
 [-0.0794702   0.51655629 -0.40397351]
 [ 0.609375    0.0625      0.328125  ]
 [ 0.33640553 -0.4562212  -0.20737327]]

L2 normalized data:
[[ 0.75765788 -0.43082507  0.49024922]
 [-0.12030718  0.78199664 -0.61156148]
 [ 0.87690281  0.08993875  0.47217844]
 [ 0.55734935 -0.75585734 -0.34357152]]
"""
