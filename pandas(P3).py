import pandas as pd

df=pd.read_csv("data.csv")
#,index_col="Name
#print(df.to_string())

#SELECTION BY COLUMN
#print(df["Height"])

#SELECTION BY ROW/S
#print(df.loc["Clefable":"Oddish",["Height","Weight"]])
#print(df.iloc[0:11])

#pokemon=input("Enter a Pokemon name:")

#try:
#    print(df.loc[pokemon])
#except KeyError:
#    print(f"{pokemon} not found")
#tall_Pokemon=df[df["Height"]>=2]
#heavy_pokemen=df[df["Weight"]>100]
#legendary_pokemen=df[df["Legendary"]==1]
#water_pokemon=df[(df["Type1"]=="Water")|
#                 (df["Type2"]=="Water")]

#ff_pokemon=df[(df["Type1"]=="Fire")&(df["Type2"]=="Flying")]

#Whole dataframe
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())

#Single column
#print(df["Height"].mean())
#print(df["Height"].sum())
#print(df["Height"].min())
#print(df["Height"].max())
#print(df["Type2"].count())

#group=df.groupby("Type1")
#print(group["Height"].mean())
#print(group["Height"].sum())
#print(group["Height"].min())
#print(group["Height"].max())
#print(group["Height"].count())

#1.Drop irrelevant columns
#df=df.drop(columns=["Legendary","No"])

#2.Handle missing data
#df=df.dropna(subset=["Type2"])
#df=df.fillna({"Type2": "None"})

#3.Fix inconsistent values
#df["Type1"]=df["Type1"].replace({"Grass":"GRASS",
#                                 "Fire":"FIRE",
#                                 "Water":"WATER"})

#4.Standardize text
#df["Name"]=df["Name"].str.lower()

#5.Fix data types
#df["Legendary"]=df["Legendary"].astype(bool)

#6.Remove duplicate values
df=df.drop_duplicates()

print(df.to_string())