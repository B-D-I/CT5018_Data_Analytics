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

# 2014 & 2015
mean_unemployment = crime1415_area_totals.iloc[:, 1]
mean_employment = crime1415_area_totals.iloc[:, 2]
mean_income = crime1415_area_totals.iloc[:, 3]
mean_burglaries = crime1415_area_totals.iloc[:, 4]
mean_robberies = crime1415_area_totals.iloc[:, 5]
mean_thefts = crime1415_area_totals.iloc[:, 6]
mean_combined = crime1415_area_totals.iloc[:, 7]


# BAR GRAPH
multi_bar_graph(countiesShort, mean_combined, mean_thefts, mean_burglaries, mean_robberies, "Locations", "All Crimes", "2014-2015 Mean Combined Theft Crimes")
# bar_graph(countiesShort, mean_robberies, "Locations", "Robberies", "2014-2015 Mean Robberies")
# bar_graph(countiesShort, mean_burglaries, "Locations", "Burglaries", "2014-2015 Mean Burglaries")
# bar_graph(countiesShort, mean_thefts, "Locations", "Thefts", "2014-2015 Mean Thefts")

# COMPARE PER CAPITA
non_per_cap_total_crime = allData.iloc[74:94, 30]
per_cap_total_crime = allDataNew.iloc[83:103, 35]
# multi_bar_graph(countiesShort, non_per_cap_total_crime, non_per_cap_total_crime, per_cap_total_crime,
#                 per_cap_total_crime, "Locations", "All Crimes", "2014-2015 Theft Crimes Per Capita Comparison")

















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




Transposed = pd.read_csv('CrimesTransposed.csv', index_col=0)
burgTime1 = Transposed.iloc[1:23, 0:4]
burgTime2 = Transposed.iloc[1:23, 4:8]
burgTime3 = Transposed.iloc[1:23, 8:12]
burgTime4 = Transposed.iloc[1:23, 12:16]
burgTime5 = Transposed.iloc[1:23, 16:20]

