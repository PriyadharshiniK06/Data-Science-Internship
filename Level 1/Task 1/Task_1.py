#%%
#importing the libraries
import pandas as pd
import matplotlib.pyplot as p     
#Loading the dataset                                 
df =pd.read_csv("Dataset .csv")
#Checking the number of rows and columns
print("Number of Rows and Columns: ",df.shape)
#Getting all the column names
print("Column names : ",df.columns)
#Checking for any missing or null values in each column
#After replacing the null values in the Cuisines column checking for any other null values in the column 
print("Checking the missing values in the column Cuisines after replacing : ",df["Cuisines"].isnull().sum())
#To Perform Data Type conversion
#First checking for the data type of each column
print("data Types of each column: ")
print(df.dtypes)
#To Analyze the distribution of the target variable "Aggregate Rating" and identify any class imbalance
#To check for class imbalance
rating_count=df["Aggregate rating"].value_counts().sort_index()
print(rating_count)
#To analyze the distribution
print("Aggregate Rating: ")
print(df["Aggregate rating"].describe())
with open("task1_text_output.txt","w") as f:
    f.write("TASK 1: DATA EXPLORATION AND PREPROCESSING\n\n")
    f.write("Number of Rows and Columns: \n")
    f.write(str(df.shape)+"\n\n")
    f.write("Column Names: \n")
    f.write(str(df.columns)+"\n\n")
    f.write("Missing Values in Each Column: \n")
    f.write(str(df.isnull().sum())+"\n\n")
    f.write("Handling Missing Values: \n")
    f.write(str(df["Cuisines"].fillna("Unknown",inplace=True)))
    f.write("\nMissing Values in 'Cuisines' column after replacement: \n")
    f.write(str(df["Cuisines"].isnull().sum())+"\n")
    f.write("Data Types of each column: \n")
    f.write(str(df.dtypes))
    f.write("\nTo identify any class imbalance : \n")
    f.write(str(df["Aggregate rating"].value_counts().sort_index()))
    f.write("\nAggregate Rating: \n")
    f.write(str((df["Aggregate rating"].describe())))
#Visualizing the distribution of aggregate rating 
p.hist(df["Aggregate rating"],bins=10)
p.xlabel("Aggregate Rating")
p.ylabel("Number of Restaurants")
p.title("Distribution of Aggregate Rating")
p.savefig("Task1_Distribution_of_aggregate_rating.png",dpi=300,bbox_inches="tight")
p.show()




