import pandas as pd

# Section 1 Basic commands
print(pd.__version__)

# Section 2: DataFrame creation
my_list = [1, 2, 3, 4, 5]
df = pd.DataFrame(my_list, columns=["list"])

my_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df1 = pd.DataFrame(my_dict)

# Section 3 Data selection
var = df['A']

# Selecting multiple columns
var1 = df['A', 'B']

# Selecting Rows
var2 = df.loc[0]  # row label
var3 = df.iloc[0]  # row index

# Selecting specific values
var4 = df.at[0, 'A']

# Section 4 Data Manipulation
df['C'] = pd.Series([7, 8, 9])  # adding a column
df.drop('C', axis=1, inplace=True)  # deleting a column
df.rename(columns={'A': 'new_A'}, inplace=True)  # renaming a column
df['A'].apply(lambda x: x * 2)  # applying function to column

# Section 5 Data Cleaning
df.isnull()
# print(arr.dtype) # Checking for null values
df.dropna(inplace=True)  # Dropping null values
df.fillna(value=0, inplace=True)  # Filling null values
df.replace(1, 10, inplace=True)  # Replacing values

# Section 6 Grouping and Aggregations
df.groupby('A')  # Group By
df.agg({'A': ['min', 'max', 'mean', 'sum']})  # Aggregation

# Section 7 Merging, Joining and Concatenating
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df3 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
df4 = pd.concat([df2, df3], axis=1)  # Concatenating
df5 = pd.merge(df2, df3, on='A')  # Merging
df6 = pd.merge(df2, df3, on='A', how='left')  # Merging
df7 = pd.merge(df2, df3, on='A', how='right')  # Merging
df8 = pd.merge(df2, df3, on='A', how='outer')  # Merging
df9 = pd.merge(df2, df3, on='A', how='inner')  # Merging
df10 = pd.merge(df2, df3, on='A', how='cross')  # Merging

df11 = df1.join(df10)  # Joining
df12 = df1.join(df10, how='left')  # Joining
df13 = df1.join(df10, how='right')  # Joining
df14 = df1.join(df10, how='outer')  # Joining
df15 = df1.join(df10, how='inner')  # Joining
df16 = df1.join(df10, how='cross')  # Joining

# Section 8 Working with Dates
df['date'] = pd.to_datetime(df['date'])  # Converting to datetime
df['day'] = df['date'].dt.day  # Getting day
df['month'] = df['date'].dt.month  # Getting month
df['year'] = df['date'].dt.year  # Getting year
df['hour'] = df['date'].dt.hour  # Getting hour
df['minute'] = df['date'].dt.minute  # Getting minute
df['second'] = df['date'].dt.second  # Getting second
df['dayofweek'] = df['date'].dt.dayofweek  # Getting day of week

# Section 9 Plotting
df.plot()  # Plotting
df.hist()  # Plotting
df.boxplot()  # Plotting
df.scatter()  # Plotting
df.bar()  # Plotting
df.pie()  # Plotting
df.area()  # Plotting
df.line()  # Plotting
df.heatmap()  # Plotting
df.corr()  # Plotting
df.pivot_table()  # Plotting
df.pivot_table(index='A')  # Plotting
df.pivot_table(index='A', columns='B')  # Plotting
df.pivot_table(index='A', columns='B', values='C')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='mean')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='sum')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='max')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='min')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='count')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='std')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='var')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='median')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='sem')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='skew')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='kurt')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='mad')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='prod')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='first')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='last')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='any')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='all')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='argmax')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='argmin')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='argsort')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='nonzero')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='argwhere')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='clip')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='round')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='floor')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='ceil')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='abs')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='prod')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='pow')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='log')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='log10')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='log2')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='exp')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='sqrt')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='cbrt')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='sin')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='cos')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='tan')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='arcsin')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='arccos')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='arctan')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='sinh')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='cosh')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='tanh')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='arcsinh')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='arccosh')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='arctanh')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='deg2rad')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='rad2deg')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='erf')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='erfc')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='gamma')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='lgamma')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='digamma')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='trigamma')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='polygamma')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='factorial')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='perm')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='comb')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='rvs')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='pdf')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='cdf')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='ppf')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='stats')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='moment')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='describe')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='cov')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='corr')  # Plotting
df.pivot_table(index='A', columns='B', values='C', aggfunc='corrwith')  # Plotting

# Section 10 File I/O
df.to_csv('file.csv')  # Writing to a CSV file
df.to_excel('file.xlsx')  # Writing to an Excel file
df.to_json('file.json')  # Writing to a JSON file
df.to_pickle('file.pickle')  # Writing to a pickle file
df.to_sql('table_name', engine)  # Writing to a SQL database
df.to_feather('file.feather')  # Writing to a feather file
df.to_parquet('file.parquet')  # Writing to a parquet file
df.to_html('file.html')  # Writing to an HTML file
df.to_clipboard()  # Writing to the clipboard
df.to_clipboard(excel=True)  # Writing to the clipboard
df.to_clipboard(sep=',')  # Writing to the clipboard
df.to_clipboard(header=False)  # Writing to the clipboard
df.to_clipboard(index=False)  # Writing to the clipboard
df.to_clipboard(na_rep='NaN')  # Writing to the clipboard
df.to_clipboard(float_format='%.2f')  # Writing to the clipboard
df.to_clipboard(columns=['A', 'B'])  # Writing to the clipboard
df.to_clipboard(header=False, index=False)  # Writing to the clipboard
df.to_clipboard(header=False, index=False, na_rep='NaN')  # Writing to the clipboard
df.to_clipboard(header=False, index=False, na_rep='NaN', float_format='%.2f')  # Writing to the clipboard
df.to_clipboard(header=False, index=False, na_rep='NaN', float_format='%.2f', columns=['A', 'B'])  # Writing to the clipboard
df.to_clipboard(sep=',', header=False, index=False, na_rep='NaN', float_format='%.2f', columns=['A', 'B'])  # Writing to the clipboard

pd.read_csv('file.csv')  # Reading from a CSV file
pd.read_excel('file.xlsx')  # Reading from an Excel file
pd.read_json('file.json')  # Reading from a JSON file
pd.read_pickle('file.pickle')  # Reading from a pickle file
pd.read_sql('table_name', engine)  # Reading from a SQL database
pd.read_feather('file.feather')  # Reading from a feather file
pd.read_parquet('file.parquet')  # Reading from a parquet file
pd.read_html('file.html')  # Reading from an HTML file
pd.read_clipboard()  # Reading from the clipboard
pd.read_clipboard(sep=',')  # Reading from the clipboard
pd.read_clipboard(header=False)  # Reading from the clipboard
pd.read_clipboard(index=False)  # Reading from the clipboard
pd.read_clipboard(na_rep='NaN')  # Reading from the clipboard
pd.read_clipboard(float_format='%.2f')  # Reading from the clipboard
pd.read_clipboard(columns=['A', 'B'])  # Reading from the clipboard
pd.read_clipboard(header=False, index=False)  # Reading from the clipboard
pd.read_clipboard(header=False, index=False, na_rep='NaN')  # Reading from the clipboard
pd.read_clipboard(header=False, index=False, na_rep='NaN', float_format='%.2f')  # Reading from the clipboard
pd.read_clipboard(header=False, index=False, na_rep='NaN', float_format='%.2f', columns=['A', 'B'])  # Reading from the clipboard
pd.read_clipboard(sep=',', header=False, index=False, na_rep='NaN', float_format='%.2f', columns=['A', 'B'])  # Reading from the clipboard

# Section 11 Miscellaneous
df.info()  # Getting information about the DataFrame
df.describe()  # Getting summary statistics of the DataFrame
df.memory_usage()  # Getting the memory usage of the DataFrame
df.memory_usage(deep=True)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True, include_types=None)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True, include_types=None, exclude_types=None)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True, include_types=None, exclude_types=None, verbose=True)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True, include_types=None, exclude_types=None, verbose=True, max_rows=10)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True, include_types=None, exclude_types=None, verbose=True, max_rows=10, max_cols=10)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True, include_types=None, exclude_types=None, verbose=True, max_rows=10, max_cols=10, max_depth=10)  # Getting the memory usage of the DataFrame
df.memory_usage(index=True, deep=True, numeric_only=True, include_types=None, exclude_types=None, verbose=True, max_rows=10, max_cols=10, max_depth=10, max_cols_per_depth=10)
