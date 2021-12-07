import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_columns', None)


def barGraph(x, y, xLabel, yLabel, title):
    plt.bar(x, y)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()

def boxPlot(data, yLabel, title):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(data)
    # iMedian = data.median()
    # iMax = data.max()
    # iMin = data.min()
    # l_quartile = data.quantile(q=0.25)
    # h_quartile = data.quantile(q=0.75)

    plt.ylabel(yLabel)
    plt.title(title)

    plt.show()
    # # # annotations (1st Q)
    # # ax.annotate('$1^{st}Q$', xy=(1, l_quartile),
    # # # align
    # # xytext = (3, 0.2),
    # # # arrow
    # # arrowprops = dict(facecolor='red', shrink=0.01),)
    # # #
    # # ax.annotate('$2^{nd}Q$', xy=(1, iMedian),
    # # xytext = (1.12, 4),
    # # arrowprops = dict(facecolor='blue', shrink=0.06),)
    # # #
    # # ax.annotate('$3^{rd}Q$', xy=(1, h_quartile),
    # # xytext = (1.12, 7),
    # # arrowprops = dict(facecolor='black', shrink=0.06),)

