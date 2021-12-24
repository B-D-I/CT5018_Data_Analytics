
import pandas as pd
import statistics
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from math import sqrt
from scipy.stats import t
from scipy.stats import skew
from scipy.stats import ttest_1samp
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from sklearn.naive_bayes import GaussianNB
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option('display.max_columns', None)

allData = pd.read_excel("./DataSheets/AllData.xlsx", na_values="")
crimesTransposed = pd.read_csv("./DataSheets/CrimesTransposed.csv", na_values="")
# time series
Transposed = pd.read_csv('./DataSheets/CrimesTransposed.csv', index_col=0)

allDataNew = pd.read_excel("./DataSheets/AllDataUpdateCompletePerCap.xlsx", na_values="")
# AllDataNew:
# BURGLARY: row 2:22 | ROBBERY: row 29:49 | THEFT: row 56:76
# 2014: column 8:20 | 2015: column 20:32


crime14NotPerCap = pd.read_csv("./DataSheets/2014(notPerCapita).csv", na_values="")
crime14_area_totals = pd.read_csv("./DataSheets/2014.csv", na_values="")
crime15_area_totals = pd.read_csv("./DataSheets/2015.csv", na_values="")

crime1415_area_totals = pd.read_csv("./DataSheets/2014&2015.csv", na_values="")
# 2014 & 2015
mean_unemployment = crime1415_area_totals.iloc[:, 1]
mean_employment = crime1415_area_totals.iloc[:, 2]
mean_income = crime1415_area_totals.iloc[:, 3]
mean_burglaries = crime1415_area_totals.iloc[:, 4]
mean_robberies = crime1415_area_totals.iloc[:, 5]
mean_thefts = crime1415_area_totals.iloc[:, 6]
mean_combined = crime1415_area_totals.iloc[:, 7]


crime1415_employmentNominal = pd.read_csv("./DataSheets/2014&15EmployNominal.csv", na_values="")
crime1415_crimeNominal = pd.read_csv("./DataSheets/2014&15CrimeNominal.csv", na_values="")

location_timeseries = pd.read_csv("./DataSheets/locationFullTimeSeries.csv", index_col=0)
location_timeseries.index.name = None
location_timeseries.reset_index(inplace=True)
dorset_timeseries = location_timeseries.iloc[:, 1:6]

# for missing month time-series analysis:
df = pd.read_csv("./DataSheets/transposeInd.csv", index_col=0)
df.index.name = None
df.reset_index(inplace=True)

# COUNTIES (excluding National)
counties = allData.iloc[2:22, 0]
countiesShort = ["Durh", "NYrk", "SYrk", "GMan", "Ches", "Lanc", "Derb", "Leic", "Linc", "Warw", "WMid", "Essx", "Hert",
                 "Suff", "Lond", "TVal", "Hamp", "Kent", "Glos", "Dors"]


burglary = crime1415_area_totals.iloc[:, 4]
robbery = crime1415_area_totals.iloc[:, 5]
theft = crime1415_area_totals.iloc[:, 6]
combined = crime1415_area_totals.iloc[:, 7]

# SQUARE ROOT AND NATURAL LOG TRANSFORMATIONS
combined_sqrt = np.sqrt(combined)
combined_log = np.log(combined)
burglary_sqrt = np.sqrt(burglary)
burglary_log = np.log(burglary)
robbery_sqrt = np.sqrt(robbery)
robbery_log = np.log(robbery)
theft_sqrt = np.sqrt(theft)
theft_log = np.log(theft)

# HYPOTHESIS
hypothesis_one = pd.read_csv("./DataSheets/Hypothesis.csv")

# Linear Regression
regression_data = pd.read_csv("./DataSheets/linearRegression.csv", index_col=0)

# Association Rules
encoded_data = pd.read_csv("./DataSheets/dataEncoded.csv")

# Classification
classified_data = pd.read_csv("./DataSheets/EncodedClassification.csv")

