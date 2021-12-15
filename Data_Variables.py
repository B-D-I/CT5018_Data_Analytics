import numpy as np
import pandas as pd

from Time_Series_Functions import *

allData = pd.read_excel("AllData.xlsx", na_values="")
crimesTransposed = pd.read_csv("CrimesTransposed.csv", na_values="")


allDataNew = pd.read_excel("AllDataUpdateCompletePerCap.xlsx", na_values="")

crime14NotPerCap = pd.read_csv("2014(notPerCapita).csv", na_values="")
crime14_area_totals = pd.read_csv("2014.csv", na_values="")
crime14EmpCategorial = pd.read_csv("crime14EmpCat.csv", na_values="")
crime14CrimeCat = pd.read_csv("crime14CrimeCat.csv", na_values="")

crime15_area_totals = pd.read_csv("2015.csv", na_values="")
crime1415_area_totals = pd.read_csv("2014&2015.csv", na_values="")


# for missing month time-series analysis:
df = pd.read_csv("transposeInd.csv", index_col=0)
df.index.name = None
df.reset_index(inplace=True)

# COUNTIES (excluding National)
counties = allData.iloc[2:22, 0]
countiesShort = ["Durh", "NYrk", "SYrk", "GMan", "Ches", "Lanc", "Derb", "Leic", "Linc", "Warw", "WMid", "Essx", "Hert",
                 "Suff", "Lond", "TVal", "Hamp", "Kent", "Glos", "Dors"]

# AllDataNew:
# BURGLARY: row 2:22 | ROBBERY: row 29:49 | THEFT: row 56:76
# 2014: column 8:20 | 2015: column 20:32
#print(allDataNew.iloc[2:22, 20:32])

# 2014 & 2015
# mean unemployment: col 1 -> mean theft: col 6
print(crime1415_area_totals.iloc[:,6])

# total theft act crimes 14&15 with per-capita
combinedTotal14PerCap = allData.iloc[74:99, 60]
combinedTotal15PerCap = allData.iloc[74:99, 61]
combinedTotal14and15PerCap = allData.iloc[74:99, 62]
# total theft crimes 14&15
combinedTotal14and15 = allData.iloc[74:99, 30]


# UNEMPLOYMENT COLUMNS (per capita)
unemp14 = allData.iloc[2:22, 34]
meanUnemp14 = allData.iloc[23, 34]
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

Transposed = pd.read_csv('CrimesTransposed.csv', index_col=0)
burgTime1 = Transposed.iloc[1:23, 0:4]
burgTime2 = Transposed.iloc[1:23, 4:8]
burgTime3 = Transposed.iloc[1:23, 8:12]
burgTime4 = Transposed.iloc[1:23, 12:16]
burgTime5 = Transposed.iloc[1:23, 16:20]

robbTime1 = Transposed.iloc[28:52, 0:4]
robbTime2 = Transposed.iloc[28:52, 4:8]
robbTime3 = Transposed.iloc[28:52, 8:12]
robbTime4 = Transposed.iloc[28:52, 12:16]
robbTime5 = Transposed.iloc[28:52, 16:20]

# mean burglary
mean_burg2014To2015 = allData.iloc[23, 36:60]
mean_burg2014 = allData.iloc[23, 36:48]
# Total crime array for box-plots
BurglaryTotals = [BurglaryTotals14, BurglaryTotals15]
RobberyTotals = [RobberyTotals14, RobberyTotals15]
TheftTotals = [TheftTotals14, TheftTotals15]


# Income
income14 = crime14_area_totals.iloc[:, 3]