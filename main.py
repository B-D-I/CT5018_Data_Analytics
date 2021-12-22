
from Time_Series_Functions import *


# # # #  DESCRIPTIVE # # # #
# central_tendencies("median", crime1415_area_totals.iloc[:, ])
# dispersion("std", crime1415_area_totals.iloc[:, ])


# BAR GRAPH
# multi_bar_graph(countiesShort, mean_combined, "Combined", mean_thefts, "Theft", mean_burglaries, "Burglary",
#               mean_robberies, "Robbery", "Locations", "All Crimes", "2014-2015 Mean Combined Theft Crimes")


# COMPARE PER CAPITA
# non_per_cap_total_crime = allData.iloc[74:94, 30]
# per_cap_total_crime = allDataNew.iloc[83:103, 35]
# multi_bar_graph(countiesShort, non_per_cap_total_crime, "Not Per-capita",
#                 per_cap_total_crime, "Per-capita", "Locations", "All Crimes",
#                 "2014-2015 Theft-Act Crimes Per Capita Comparison")


# HOW THEFT ACT CRIMES ARE DIVIDED (pie chart)
# crimes = (20716, 7977, 129653)
# crimeLabels = ["Burglary", "Robbery", "Theft"]
# plt.pie(crimes, labels=crimeLabels)
# plt.show()


# Line graphs
# sns.set_style('whitegrid')
# sns.lmplot("Earnings", "Employment", crime1415_crimeNominal, hue="Measurement of Theft Crime ", fit_reg=False,
# palette=dict(High="r", Medium="m", Low="g"))
# sns.lmplot("Earnings", "Unemployment", crime1415_crimeNominal, hue="Measurement of Theft Crime ", fit_reg=False,
# palette=dict(High="r", Medium="m", Low="g"))
# plt.show()


# COVARIANCE & CORRELATION
# relational("covariance", crime14NotPerCap)
# relational("correlation", crime14NotPerCap)
# ^^ APPEARS TO HAVE POSITIVE CORRELATION ONLY WHEN PER CAPITA NOT TAKEN INTO ACCOUNT

# relational("cov", crime1415_area_totals)
# relational("corr", crime1415_area_totals)


# HISTOGRAMS FOR SKEW AND TRANSFORMATION
# print(skew(combined, bias=False))
# plt.hist(combined)
# plt.hist(combined_sqrt)
# plt.hist(combined_log)
# plt.show()


# HYPOTHESIS

# input confidence value % to check, e.g. 95
confidence = float(input('confidence interval in %: '))

# run independent t-test
# test between sample 1 and sample 2 (high / low)
ind_t_test = stats.ttest_ind(hypothesis_one.Combined[hypothesis_one.Areas == 'High-Unemployment/Low-Employment'],
                             hypothesis_one.Combined[hypothesis_one.Areas == 'Low-Unemployment/High-Employment'])

# T and P values
tvalue = ind_t_test[0]
pvalue = ind_t_test[1]

print('results of independent t-test are: \n\tt-value = {:4.3f}\n\tp-value = {:4.3f}'.format(tvalue, pvalue))

# check confidence
if(pvalue > (1 - confidence/100)):
    print('\nH0 => u1 - u2 = 0\n\t Confidence: '+str(confidence), '%')
else:
    print('\nH1 => u1 - u2 !=0\n\t Confidence: '+str(confidence), '%')









# # # # TIME SERIES # # # #

# Display timeseries rolling mean, std, and autocorrelation
# timeseries = pd.read_csv('CrimesTransposed.csv', index_col=0)
# burglary_timeseries = timeseries.iloc[1:23, 2]
# robbery_timeseries = timeseries.iloc[28:50, 10]
# theft_timeseries = timeseries.iloc[55:77, 16]
# visualiseTimeseries(theft_timeseries, 12, "West Midlands Theft")


# time series function
#time_series(df, "ARMA", "2014-01-01", 22, "2015-11-01", 4, "AREA", "Forecast")




