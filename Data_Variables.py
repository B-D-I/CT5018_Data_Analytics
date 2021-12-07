import pandas as pd

from Functions import *

allData = pd.read_excel("AllData.xlsx", na_values="")
crimesTransposed = pd.read_csv("CrimesTransposed.csv", na_values="")
crime14 = pd.read_csv("2014.csv", na_values="")
crime14NotPerCap = pd.read_csv("2014(notPerCapita).csv", na_values="")
crime14EmpCatergorial = pd.read_csv("crime14EmpCat..csv", na_values="")
crime14CrimeCat = pd.read_csv("crime14CrimeCat.csv", na_values="")

# COUNTIES (excluding National)
counties = allData.iloc[2:22, 0]
countiesShort = ["Durh", "NYrk", "SYrk", "GMan", "Ches", "Lanc", "Derb", "Leic", "Linc", "Warw", "WMid", "Essx", "Hert",
                 "Suff", "Lond", "TVal", "Hamp", "Kent", "Glos", "Dors"]

# total theft act crimes 14&15 with per-capita
combinedTotal14PerCap = allData.iloc[74:99, 60]
combinedTotal15PerCap = allData.iloc[74:99, 61]
combinedTotal14and15PerCap = allData.iloc[74:99, 62]
# total theft crimes 14&15
combinedTotal14and15 = allData.iloc[74:99, 30]

# UNEMPLOYMENT COLUMNS (per capita)
unemp14 = allData.iloc[2:22, 34]
unemp15 = allData.iloc[2:22, 35]
unempBothAverage = allData.iloc[2:22, 72]
allUnemp = [unemp14, unemp15, unempBothAverage]


# TOTAL CRIMES FOR EACH CRIME TYPE (per capita)
# combined
BurglaryTotals14 = allData.iloc[2:22, 60]
BurglaryTotals15 = allData.iloc[2:22, 61]
RobberyTotals14 = allData.iloc[26:46, 60]
RobberyTotals15 = allData.iloc[26:46, 61]
TheftTotals14 = allData.iloc[50:70, 60]
TheftTotals15 = allData.iloc[50:70, 61]
# Total crime array for box-plots
BurglaryTotals = [BurglaryTotals14, BurglaryTotals15]
RobberyTotals = [RobberyTotals14, RobberyTotals15]
TheftTotals = [TheftTotals14, TheftTotals15]

# Income
income14 = crime14.iloc[:, 3]