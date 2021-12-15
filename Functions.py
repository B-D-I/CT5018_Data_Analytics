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

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

pd.set_option('display.max_columns', None)


def bar_graph(x, y, xLabel, yLabel, title):
    plt.bar(x, y)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


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
    ax.boxplot(data)
    # iMedian = data.median()
    # iMax = data.max()
    # iMin = data.min()
    # l_quartile = data.quantile(q=0.25)
    # h_quartile = data.quantile(q=0.75)

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

    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


