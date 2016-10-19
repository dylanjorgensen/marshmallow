# Resources
# - http://pandas.pydata.org/pandas-docs/stable/merging.html



# This will merge column 1 and 15
new = df.iloc[:,[1,15]]

# This will merge the column with the index 'rain' and 'fog'
new = df.loc[:,['rain','fog']]


# this will turn the dataframe into a matrix (like the type for machine learning)
numpyMatrix = df.as_matrix()


y_sting = y_np.tolist()