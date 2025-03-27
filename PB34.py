# Read this csv file car data.csv and display the basic information like memory and data types for this data frame.
import pandas as pd
import numpy as np

df = pd.read_csv('car data.csv')
print(df.info())

#1.How Many ritz car are there with kms driven more than 30000km.
print(df[(df['Car_Name']=='ritz') & (df['Kms_Driven']>30000)].shape[0])

#2.How many Petrol cars are of the year 2017 and whose selling price > 10 lakhs.
print(df[(df['Fuel_Type']=='Petrol') & (df['Year']==2017) & (df['Selling_Price']>10)].shape[0])

#3.How many swi cars are there with selling price < 4 Lakhs.
print(df[(df["Car_Name"]=='swift') & (df['Selling_Price'] < 4)].shape[0])

#4.How many Automa c Transmission Petrol Car are of the year 2015 whose selling price is > 10 Lakhs.
print(df[(df['Transmission'] == 'Automatic') & (df['Fuel_Type']=='Petrol') & (df['Year']==2015) & (df['Selling_Price']>10)].shape[0])

#5.List out Vehicles with Automa c Transmission and selling price < 1 Lakh.
print(df[(df["Transmission"]=='Automatic') & df['Selling_Price']<1].shape[0])

#6.How Many Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included).
print(df[(df['Fuel_Type']=='Petrol') & (df['Kms_Driven']>50000) & (df['Year'] >= 2010) & (df['Year']<=2015) ].shape[0])

#7.List out the cars whose price difference between present price and selling price is > 15 lakhs.
print(df[df['Present_Price']-df['Selling_Price']>15].shape[0])

#8.How many Petrol vehicles are there whose kms driven < 5000km and selling price < 50000.
print(df[(df['Fuel_Type']=="Petrol") & (df['Kms_Driven']<5000) & (df['Selling_Price']<0.5)].shape[0])