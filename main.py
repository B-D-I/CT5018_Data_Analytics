import matplotlib.pyplot as plt

from Data_Variables import *

# TO DO:

# CREATE A TIMESERIES WITH MEAN THEFT ACT CRIMES, WITH UNEMPLOYMENT, EMPLOYMENT, INCOME - then produce a line graph with
# all variables to see if any relationship
# NEED KEY FOR THE BAR GRAPH COLORS
# CREATE A NOMINAL 2014 & 2015 with high / low varibales


# ? HYPOTHESIS:
# H0: Unemployment does not increase theft crime / H1: Unemployment does increase theft crimes /
# H0: Low earnings does not increase theft crime / H1: Low earnings does increase theft crime / H4: Neither make any difference
# DATA FLOW DIAGRAM


#central_tendencies("mean", crime14_area_totals.iloc[:, ])
#dispersion("std", crime1415_area_totals.iloc[:, ])


# line graph crimes 14 - 15 (until Nov)    - this shows all locations are seasonal and within this timeframe follow no trend
# burgTime1.plot()
# burgTime2.plot()
# burgTime3.plot()
# burgTime4.plot()
# burgTime5.plot()
# plt.show()


# COVARIANCE & CORRELATION

# relational("covariance", crime14NotPerCap)
# relational("correlation", crime14NotPerCap)
# ^^ APPEARS TO HAVE POSITIVE CORRELATION ONLY WHEN PER CAPITA NOT TAKEN INTO ACCOUNT

# relational("covariance", crime14_area_totals)
# relational("correlation", crime14_area_totals)

# relational("covariance", crime15)
# relational("correlation", crime15)



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
# boxPlot(BurglaryTotals14, "Crime Amount", "Burglary Per Capita")
# boxPlot(RobberyTotals14, "Crime Amount", "Robbery Per Capita")
# boxPlot(TheftTotals14, "Crime Amount", "Theft Per Capita")
# plt.xlabel("Counties")
# plt.ylabel("")
# plt.title("Theft Act Crimes 2014 Per-Capita")
# plt.legend()
# plt.show()




# THESE PLOTS SUGGEST MOST THEFT ACT CRIMES OCCUR IN AREAS WHERE UNEMPLOYMENT IS AVERAGE AND EARNINGS ARE LOW-AVERAGE
# sns.set_style('whitegrid')
# sns.lmplot("Earnings", "Unemployment", crime14CrimeCat, hue="Robbery", fit_reg=False, palette=dict(High="r", Medium="m", Low="g"))
# sns.lmplot("Earnings", "Unemployment", crime14CrimeCat, hue="Burglary", fit_reg=False, palette=dict(High="r", Medium="m", Low="g"))
# sns.lmplot("Earnings", "Unemployment", crime14CrimeCat, hue="Theft", fit_reg=False, palette=dict(High="r", Medium="m", Low="g"))
# plt.show()









# Display timeseries rolling mean, std, and autocorrelation
# timeseries = pd.read_csv('CrimesTransposed.csv', index_col=0)
# burglary_timeseries = timeseries.iloc[1:23, 2]
# robbery_timeseries = timeseries.iloc[28:50, 10]
# theft_timeseries = timeseries.iloc[55:77, 16]
# visualiseTimeseries(theft_timeseries, 12, "West Midlands Theft")


# time series function
#time_series(df, "ARMA", "2014-01-01", 22, "2015-11-01", 4, "AREA", "Forecast")




