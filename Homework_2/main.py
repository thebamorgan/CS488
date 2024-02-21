import pandas as pd
import matplotlib as mp
import numpy as np

columnAtrributes = ['sepal_L', 'speal_W', 'petal_L', 'petal_W', 'classification']


iris = pd.read_csv('./Iris_dataset/iris.data', sep=",", header=None, names=columnAtrributes)

groupedData = iris.groupby('classification')



print(groupedData)

# subsets = {}
# for group_name, group_df in groupedData:
#     subsets[group_name] = group_df
# print(subsets.keys)

# for key, subset_df in subsets.items():
#     print(f"Subset for {key}:")
#     print(subset_df)
#     print()  # Add an empty line for separation between subsets


# Count the number of rows in each subset DataFrame
# subset_counts = {}
# for key, subset_df in subsets.items():
#     subset_counts[key] = len(subset_df)

# # Print the counts
# for key, count in subset_counts.items():
#     print(f"Subset for {key}: {count} rows")

# i) Correlation coefficient – display correlation matrix as heat map (as in demo)
    
    # r = np.corrcoef()