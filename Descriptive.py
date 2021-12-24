from Data_Variables import *


def central_tendencies(measure, data):
    if measure == "mean":
        print(data.mean())
    elif measure == "median":
        print(data.median())
    elif measure == "mode":
        print(data.mode())


def dispersion(measure, data):
    if measure == "var":
        print(data.var())
    elif measure == "std":
        print(data.std())


def bar_graph(x, y, xLabel, yLabel, title):
    plt.bar(x, y)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


def multi_bar_graph(x, y, bar1Title, y2, bar2Title, y3, bar3Title, y4, bar4Title, xLabel, yLabel, title):
    bar1 = plt.bar(x, y, color="#999999")
    bar2 = plt.bar(x, y2, color="#46a41e")
    bar3 = plt.bar(x, y3, color="#2986cc")
    bar4 = plt.bar(x, y4, color="#e97c0b")
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.legend((bar1, bar2, bar3, bar4), (bar1Title, bar2Title, bar3Title, bar4Title))
    plt.title(title)
    plt.show()


def relational(measure, data):
    if measure == "cov":
        print(data.cov())
    elif measure == "corr":
        print(data.corr())
        cormatrix = data.corr()
        cormatrix = cormatrix.stack()
        cormatrix = cormatrix.reindex(cormatrix.abs().sort_values(ascending=False).index).reset_index()
        print(cormatrix)
        scatter_matrix(data, diagonal="kde")
        plt.figure(figsize=(7, 7))
        sns.heatmap(data.corr(), annot=True, fmt='.0%')
        plt.show()


def percentile(data, percent):
    print(np.percentile(data, percent))


def box_plot(data, yLabel, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(data, vert=False)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


# # # #  DESCRIPTIVE # # # #

central_tendencies("median", crime1415_area_totals.iloc[:, ])
dispersion("std", crime1415_area_totals.iloc[:, ])


# BAR GRAPH
multi_bar_graph(countiesShort, mean_combined, "Combined", mean_thefts, "Theft", mean_burglaries, "Burglary",
              mean_robberies, "Robbery", "Locations", "All Crimes", "2014-2015 Mean Combined Theft Crimes")


# COMPARE PER CAPITA
non_per_cap_total_crime = allData.iloc[74:94, 30]
per_cap_total_crime = allDataNew.iloc[83:103, 35]
multi_bar_graph(countiesShort, non_per_cap_total_crime, "Not Per-capita",
                per_cap_total_crime, "Per-capita", "Locations", "All Crimes",
                "2014-2015 Theft-Act Crimes Per Capita Comparison")


# HOW THEFT ACT CRIMES ARE DIVIDED (pie chart)
crimes = (20716, 7977, 129653)
crimeLabels = ["Burglary", "Robbery", "Theft"]
plt.pie(crimes, labels=crimeLabels)
plt.show()


# LINE GRAPHS
sns.set_style('whitegrid')
sns.lmplot("Earnings", "Employment", crime1415_crimeNominal, hue="Measurement of Theft Crime ", fit_reg=False,
palette=dict(High="r", Medium="m", Low="g"))
sns.lmplot("Earnings", "Unemployment", crime1415_crimeNominal, hue="Measurement of Theft Crime ", fit_reg=False,
palette=dict(High="r", Medium="m", Low="g"))
plt.show()


# COVARIANCE & CORRELATION
relational("cov", crime1415_area_totals)
relational("corr", crime1415_area_totals)


# HISTOGRAMS FOR SKEW AND TRANSFORMATION
print(skew(combined, bias=False))
plt.hist(combined)
plt.hist(combined_sqrt)
plt.hist(combined_sqrt)
plt.show()