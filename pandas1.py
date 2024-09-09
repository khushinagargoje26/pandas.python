import pandas as pd
import numpy as np
#1Reading Data from CSV
df_from_csv = pd.read_csv(r"C:\Users\khush\OneDrive\Desktop\crypto\consolidated_coin_data.csv")
print("DataFrames from CSV:")
print(df_from_csv)

#2Creating a Series
data=[10,20,30,50,70,60]
index=['a','b','c','d','e','f']
series=pd.Series(data,index=index)
print("Series:")
print(series)

#Creating DataFrame
data={
    'Name':['john','Anna','Peter','Linda','James'],
    'Age':[28,22,28,33,21],
    'City':['New York','Paris','Berlin','Tokyo','London']}
df=pd.DataFrame(data)
print("\nDataFrame:")
print(df)

#Viewing Data 
print("\nFirst 3 rows")
print(df.head(3))
print("\n Last 2 rows:")
print(df.tail(2))

#Statistics summury:
print("\nStatastics summary:") 
print(df.describe())


#Accesing Data
print("\n Accessing 'Name column:")
print(df['Name'])

print("\n Accesing Specific row (using loc:)")
print(df.loc[2])

print("\nAccessing specific row (using iloc):")
print(df.iloc[1])

#Filtering Data
print("\n Filtering rows where age>30:")
print(df[df['Age']>30])

#Adding a New Column
df['Salary']=[40000,50000,60000,321434,66620]
print("\nDataFrame after adding 'Salary' Column:")
print(df)

#Updating Data
df.loc[df['Name'] == 'Anna', 'Age'] = 23
print("\nDataFrame after updating age of Anna:" )
print(df)

#Deleting Data  
df=df.drop('Salary',axis=1)
print("\n DataFrame after dropping 'Salary'column:")
print(df) 

df = df.drop(3, axis=0)
print("\nDataFrame after dropping row with index 3:")
print(df)

# 10. Handling Missing Data
df.loc[4, 'Age']=np.nan # Introduce NaN
print("\nDataFrame with NaN value:")
print(df)


df_filled = df.fillna(0)  # Fill NaN with 0
print("\nDataFrame after filling NaN with 0:")
print(df_filled)


df_dropped = df.dropna()  # Drop rows with NaN
print("\nDataFrame after dropping rows with NaN:")
print(df_dropped)

# 11. Grouping Data
print("\nGrouping data by 'City' and calculating mean of 'Age':")
print(df.groupby('City')['Age'].mean())

# 12. Merging DataFrames
df1 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 23, 35]
})

df2 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Linda'],
    'City': ['New York', 'Paris', 'London']
})

merged_df = pd.merge(df1, df2, on='Name', how='inner')
print("\nMerged DataFrame:")
print(merged_df)



# 13. Concatenating DataFrames
df3 = pd.DataFrame({
    'Name': ['James', 'Robert'],
    'Age': [45, 50],
    'City': ['Toronto', 'Boston']
})

#Concatenating the two DataFrames
concatenated_df = pd.concat([df, df3])

print("\nConcatenated DataFrame:")
print(concatenated_df)



# 14. Pivoting Data
pivot_df = df.pivot(index='Name', columns='City', values='Age')
print("\nPivoted DataFrame:")
print(pivot_df)


# 15. Reshaping Data
melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'City'])
print("\nMelted DataFrame:")
print(melted_df)


# 16. Sorting Data
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age (descending):")
print(sorted_df)

# 17. Applying Functions
def add_ten(x):
    return x + 10

































