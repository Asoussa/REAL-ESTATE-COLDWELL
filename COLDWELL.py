import pandas as pd
import matplotlib.pyplot as mat

# Load the dataset from the specified Excel file
real = pd.read_excel(r"D:\My-project\Real_Estate_Sales_modified.xlsx")

# Display the first few rows of the dataset for inspection
print(real.head()) 

# Print the shape (rows, columns) and column names of the dataset
print(real.shape) 
print(real.columns) 

# Check for missing values in the dataset
print(real.isnull().sum())

# Identify rows where the 'Address' column has missing values
missing_addresses = real["Address"].isnull()
print(missing_addresses)

# Fill missing 'Address' values with "town"
real["Address"] = real["Address"].fillna("town")

# Display rows where 'Date Recorded' is missing
missing_date = real[real['Date Recorded'].isnull()]
print(missing_date)

# Drop rows where 'Date Recorded' is missing
real = real.dropna(subset=['Date Recorded'])

# Display basic statistics about the 'Assessed Value' column
print(real['Assessed Value'].mean())  # Mean value of Assessed Value
print(real['Assessed Value'].std())   # Standard deviation of Assessed Value
print(real['Assessed Value'].var())   # Variance of Assessed Value

# Filter the dataset for 'Sale Amount' between 100 million and 200 million
print(real[(real["Sale Amount"]>100000000) & (real["Sale Amount"]<200000000)])

# Find the row with the highest 'Sale Amount'
print(real[real["Sale Amount"] == real["Sale Amount"].max()])

# Replace 0 'Assessed Value' with the mean of 'Assessed Value'
real['Assessed Value'] = real['Assessed Value'].replace(0, real['Assessed Value'].mean())

# Remove rows where 'Sale Amount' is 0
real = real[real['Sale Amount'] != 0]

# Print the count of null and non-null values in the dataset
print(real.isnull().sum())
print(real.notnull().sum())

# Display general information about the dataset (e.g., data types, non-null counts)
print(real.info())

# Get summary statistics of 'Sale Amount'
print(real["Sale Amount"].describe())

# Display the number of unique values, unique categories, and value counts for 'Property Type'
print(real['Property Type'].nunique()) 
print(real['Property Type'].unique()) 
print(real['Property Type'].value_counts()) 

# Display the number of unique values, unique categories, and value counts for 'Residential Type'
print(real['Residential Type'].nunique()) 
print(real['Residential Type'].unique()) 
print(real['Residential Type'].value_counts())

# Calculate profit as 'Sale Amount' - 'Assessed Value'
real['profit'] = real['Sale Amount'] - real['Assessed Value']
print(real.columns)  # Print column names
print(real['profit'])  # Print the 'profit' column

# Convert 'Sale Amount', 'profit', 'Assessed Value', and 'Sales Ratio' to integers
real['Sale Amount'] = real['Sale Amount'].astype(int)
real['profit'] = real['profit'].astype(int)
real['Assessed Value'] = real['Assessed Value'].astype(int)
real['Sales Ratio'] = real['Sales Ratio'].astype(int)

# View rows where profit is negative
print(real[real['profit'] < 0])  # Negative profit

# Get the top 10 rows with the highest profit greater than 10 million
top_10_profit = real[real['profit'] > 1e7].nlargest(10, 'profit')
print(top_10_profit)

# Display the data types of each column
print(real.dtypes)

# Filter the rows where 'Residential Type' is 'Single Family'
print(real.groupby('Residential Type').get_group('Single Family'))

# Filter the rows where 'Property Type' is 'Residential'
print(real[real['Property Type'] == "Residential"])

# Pie chart of the 'Property Type' distribution
real['Property Type'].value_counts().plot.pie() 
mat.title('Property Type')
mat.ylabel("")  # Remove label on the y-axis for aesthetics
mat.show()

# Bar chart for the distribution of 'Residential Type'
real["Residential Type"].value_counts().plot.bar(color='orange', edgecolor='red')
mat.title('The Sum of Residential Type')
mat.xlabel('Total Residential Type')
mat.ylabel('Count')
mat.show()

# Scatter plot to visualize the relationship between 'Assessed Value' and 'Sale Amount'
real.plot(kind='scatter', x='Assessed Value', y='Sale Amount', color='orange', alpha=0.5, figsize=(10, 6))
mat.title('Assessed Value vs Sale Amount')
mat.xlabel('Assessed Value')
mat.ylabel('Sale Amount')
mat.show()

# Save the dataset to a CSV file
real.to_csv(r'D:\My-project\COLDWELL-BANKER.csv')
