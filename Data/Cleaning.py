 import pandas as pd

#Read the raw data scraped from the website
df = pd.read_csv("books.csv")

#Clean prices to float
df["price"] = df["price"].str.replace("£", "").astype(float)


#Clean ratings and convert to numbers
df["rating"] = df["rating"].str.replace("star-rating", "").str.strip()
rating_map = {"One": 1,"Two": 2,"Three": 3,"Four": 4,"Five": 5}
df["rating"] = df["rating"].map(rating_map)


#Remove duplicate
df.drop_duplicates(inplace=True)

#Strip extra spaces from book titles
df["title"] = df["title"].str.strip()

#Drop rows with missing values
df.dropna(inplace=True)


#Save cleaned data to a new CSV file
df.to_csv("books_clean.csv", index=False)



