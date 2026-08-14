#Feature Engineering
#1. Length of the columns like restaurant name or address
import pandas as pd
from io import StringIO
df=pd.read_csv("Dataset .csv")
#Checking the column names
df.columns
#Creating new columns for viewing the length of the column values
df["Restaurant_Name_lengths"]=df["Restaurant Name"].str.len()
df["Address_lengths"]=df["Address"].str.len()
print(df[["Restaurant Name","Restaurant_Name_lengths","Address","Address_lengths"]].head(5))
#Encoding the categorical variables in boolean columns 
df["Has_Table_Booking_Encoded"]=df["Has Table booking"].map({"Yes":1,"No":0})
df["Has_Online_Delivery_Encoded"]=df["Has Online delivery"].map({"Yes":1,"No":0})
print(df[["Has_Table_Booking_Encoded","Has Table booking","Has_Online_Delivery_Encoded","Has Online delivery"]].head(5))
#checking all the columns are viewed and checking that  new columns are added 
df.info()
with open("Task_6_output_text.txt","w") as f:
    f.write("Feature Engineering\n\n")
    f.write("Checking the column names: \n\n")
    f.write(str(df.columns))
    f.write("\n")
    f.write("Creating new columns for viewing the length of the column values: \n\n")
    f.write(str(df[["Restaurant Name","Restaurant_Name_lengths","Address","Address_lengths"]].head(5)))
    f.write("\n")
    f.write("Encoding the categorical variables in boolean columns:\n\n")
    f.write(str(df[["Has_Table_Booking_Encoded","Has Table booking","Has_Online_Delivery_Encoded","Has Online delivery"]].head(5)))
    f.write("\n")
    f.write("Checking all the columns are viewed and checking that new columns are added:\n\n")
    buffer=StringIO()
    df.info(buf=buffer)
    f.write(buffer.getvalue())
    