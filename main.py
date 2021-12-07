import matplotlib.pyplot as plt

from Data_Variables import *


# TIME SERIES TO PLOT MISSING DATA
# H0: Unemployment not increase theft crime / H1: Does have an effect on theft crimes / H2: Earnings etc?


# CORRELATION
# print(crime14NotPerCap.corr())
# scatter_matrix(crime14NotPerCap, diagonal="kde")
# plt.tight_layout()
# plt.show()
# ^^ APPEARS TO HAVE POSITIVE CORRELATION ONLY WHEN PER CAPITA NOT TAKEN INTO ACCOUNT

# print(crime14.corr())
# scatter_matrix(crime14, diagonal="kde")
# plt.tight_layout()
# plt.show()
# cormatrix = crime14.corr()
# cormatrix = cormatrix.stack()
# cormatrix = cormatrix.reindex(cormatrix.abs().sort_values(ascending=False).index).reset_index()
#print(cormatrix)

# THESE PLOTS SUGGEST MOST THEFT ACT CRIMES OCCUR IN AREAS WHERE UNEMPLOYMENT IS AVERAGE AND EARNINGS ARE LOW-AVERAGE
# sns.set_style('whitegrid')
# #sns.lmplot("Earnings", "Burglary", crime14EmpCatergorial, hue="Unemployment", fit_reg=False) # DONT USE
# #sns.lmplot("Earnings", "Robbery", crime14EmpCatergorial, hue="Unemployment", fit_reg=False) # DONT USE
# #sns.lmplot("Earnings", "Theft", crime14EmpCatergorial, hue="Unemployment", fit_reg=False) # DONT USE
#
# sns.lmplot("Earnings", "Unemployment", crime14CrimeCat, hue="Robbery", fit_reg=False, palette=dict(High="r", Medium="m", Low="g"))
# sns.lmplot("Earnings", "Unemployment", crime14CrimeCat, hue="Burglary", fit_reg=False, palette=dict(High="r", Medium="m", Low="g"))
# sns.lmplot("Earnings", "Unemployment", crime14CrimeCat, hue="Theft", fit_reg=False, palette=dict(High="r", Medium="m", Low="g"))
# plt.show()


# COMPARING THE TOTAL CRIMES WITH PER CAPITA
# barGraph(countiesShort, combinedTotal14and15PerCap, "Counties", "Theft Crimes", "Combined Theft Act Offences 2014-2016, per-capita")
# barGraph(countiesShort, combinedTotal14and15, "Counties", "Theft Crimes", "Combined Theft Act Offences 2014-2016")


# BAR CHART COMPARING DIFFERENCE IN TOTALS FOR YEAR 14 & 15 -- 15 HAS MISSING MONTH??
# plt.bar(countiesShort, combinedTotal14PerCap, label="2014")
# plt.bar(countiesShort, combinedTotal15PerCap, label="2015")
# plt.xlabel("Counties")
# plt.ylabel("Theft Act Offences")
# plt.title("Theft Act Offences 2014 & 2016 Per-Capita")
# plt.legend()
# plt.show()


# BAR CHART WITH BOTH YEARS TOTALS
# plt.bar(countiesShort, BurglaryTotals14, label="2014")
# plt.bar(countiesShort, BurglaryTotals15, label="2015")
# plt.xlabel("Counties")
# plt.ylabel("Burglaries")
# plt.title("Burglaries 2014 & 2015 Per-Capita")
# plt.legend()
# plt.show()

# BAR CHART OF ALL THREE CRIMES IN EACH BAR (2014)
# plt.bar(countiesShort, TheftTotals14, label="Theft")
# plt.bar(countiesShort, BurglaryTotals14, label="Burglary")
# plt.bar(countiesShort, RobberyTotals14, label="Robbery")
# plt.xlabel("Counties")
# plt.ylabel("Crimes")
# plt.title("Theft Act Offences 2014 Per-Capita")
# plt.legend()
# plt.show()


# HOW THEFT ACT CRIMES ARE DIVIDED (pie chart)
# total burglary for all counties 14&15 = 1768
# total robbery for all counties 14&15 = 40
# total theft for all counties 14&15 = 11672
# crimes = (1768, 40, 11672)
# crimeLabels = ["Burglary", "Robbery", "Theft"]
# plt.pie(crimes, labels=crimeLabels)
# plt.show()

# DISPLAY BOXPLOT TO SEE MEDIAN, AND HIGHER / LOW QUARTILES
# unemployment years:
#boxPlot(allUnemp, "Unemployment", "Unemployment Per Capita")

#boxPlot(income14, "Income", "Monthly Income")

# burglary 2014 and 2015 boxplot:
# boxPlot(BurglaryTotals, "Crime Amount", "Burglary Per Capita")
# plt.bar(countiesShort, BurglaryTotals14, label="2014")
# plt.bar(countiesShort, BurglaryTotals15, label="2015")
# plt.xlabel("Counties")
# plt.ylabel("Burglaries")
# plt.title("Burglaries 2014 & 2016 Per-Capita")
# plt.legend()
# plt.show()



#
# # TIME SERIES
# # cols: 1:19 / test rows: 1-23, then provide data for 24, and compare with 25

# # Durham
transposeBurgs = crimesTransposed.iloc[1:23, 1]
transposeRobbs = crimesTransposed.iloc[28:52, 1]
transposeTheft = crimesTransposed.iloc[55:79, 1]
transposeComb = crimesTransposed.iloc[82:106, 1]

# transposeBurgsY1 = crimesTransposed.iloc[1:13, 1]
# transposeRobbsY1 = crimesTransposed.iloc[28:40, 1]
# transposeTheftY1 = crimesTransposed.iloc[55:67, 1]
# transposeCombY1 = crimesTransposed.iloc[82:94, 1]


# ARIMA initial visualisation
df = pd.read_csv('CrimesTransposed.csv', index_col=0)
df = df.iloc[1:23, 0]

# df.index.name=None
# df.reset_index(inplace=True)
# df.set_index(['index'], inplace=True)
# df.columns = ['Durham']
# df['Durham'] = df.Durham
# df.Durham.plot(title="monthly burglary", fontsize=14)
# ^^ Line 53. AttributeError: 'Series' object has no attribute 'Durham' ^^
df.plot(title="monthly burglary", fontsize=14)
plt.show()
# # This shows that it is stationary and seasonal

timeseries = pd.read_csv('CrimesTransposed.csv', index_col=0)
timeseries = timeseries.iloc[1:23, 0]
# rolling mean / std - per x months
rolmean = timeseries.rolling(12).mean()
rolstd = timeseries.rolling(12).std()

fig = plt.figure()
orig = plt.plot(timeseries, color='blue', label='original')
mean = plt.plot(rolmean, color='red', label='Rolling Mean')
std = plt.plot(rolstd, color='black', label='Rolling Std')

plt.title('Rolling Mean & Standard Deviation ')
#plt.show()

# NEED SARIMA for seasonal        auto-regression / iteration / moving-averages -> again but with seasonal
mod = sm.tsa.statespace.SARIMAX(df, trend='n', order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = mod.fit()

# MAKE FUTURE PREDICTIONS
# start predicting from:
start = datetime.datetime.strptime("2015-11-01", "%Y-%m-%d")
# create amount of months
date_list = [start + relativedelta(months=x) for x in range(0, 2)]
# future months
future = pd.DataFrame(index=date_list, columns=df.column)
# ^^ pandas.errors.InvalidIndexError: Reindexing only valid with uniquely valued Index objects ^^

# concat the df with future dates (future dates don't have value yet)
df = pd.concat([timeseries, future])

# start= future row number start -> end
df['forecast'] = results.predict(start=24, end=27, dynamic=True)
# plot only last 24 entries (12 existing / future)
df[['Durham', 'forecast']].iloc[-22:].plot()

plt.show()


