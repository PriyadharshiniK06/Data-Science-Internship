#Price Range Analysis
#1. Determine the most common price range among all the restaurants
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Dataset .csv")
price_range_counts=df["Price range"].value_counts()
print(price_range_counts)
most_common=price_range_counts.idxmax()
print("Most Common Price Range amoung all the Restaurants: ",most_common)
#2. To calculate the average rating for each price range
avg_rating=df.groupby("Price range")["Aggregate rating"].mean()
print("The average rating for each price range: ")
print(avg_rating)
#3. To visualize the average range distribution for each price range
avg_rating.plot(kind="bar",figsize=(10,12))
plt.xlabel("Price Range")
plt.ylabel("Aggregate Rating")
plt.title("Average range distribution for each price range")
plt.savefig("Average Range Distribution for each Price Range.png",dpi=300,bbox_inches="tight")
plt.show()
#4. To identify the color that represents the highest average rating among different price range
rating_color=df.groupby("Rating color")["Aggregate rating"].mean()
highest_rating_color=rating_color.idxmax()
highest_avg_value=rating_color.max()
print("The color that represents the highest average rating among different price range: ",highest_rating_color)
print(f"The highest average rating value: {highest_avg_value:.2f}")
#Combining the price range and color
price_color_analyze=df.groupby(["Price range","Rating color"])["Aggregate rating"].mean()
print("After combining the price range and rating color that is grouped with aggregate rating: ")
print(price_color_analyze)
with open("Task_5_output_text.txt","w") as f:
    f.write("Price Range Analysis\n\n")
    f.write("Most Common Price Range amoung all the restaurants: \n")
    f.write(str(df["Price range"].value_counts().idxmax()))
    f.write("\n")
    f.write("To calculate the average rating for each price range: \n")
    f.write(str(df.groupby("Price range")["Aggregate rating"].mean()))
    f.write("\n")
    f.write("To identify the color that represents the highest average rating among different price range: \n")
    f.write(str(df.groupby("Rating color")["Aggregate rating"].mean()))
    f.write("\n")
    f.write("The color that represents the highest average rating amoung different price range: \n")
    f.write(str(df.groupby("Rating color")["Aggregate rating"].mean().idxmax()))
    f.write("\n")
    f.write("The highest average rating value is : \n")
    f.write(str(df.groupby("Rating color")["Aggregate rating"].mean().max()))
    f.write("\n")
    f.write("After combining the price range and rating color that is grouped with aggregate rating: \n")
    f.write(str(df.groupby(["Price range","Rating color"])["Aggregate rating"].mean()))