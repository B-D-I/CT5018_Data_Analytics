from Functions import *


def visualise_timeseries(data, month_amount, title_var):
    # rolling mean / std - per x months
    rolling_mean = data.rolling(month_amount).mean()
    rolling_std = data.rolling(month_amount).std()
    fig = plt.figure()
    orig = plt.plot(data, color='blue', label='original')
    mean = plt.plot(rolling_mean, color='red', label='Rolling Mean')
    std = plt.plot(rolling_std, color='black', label='Rolling Std')

    plt.title('Rolling Mean & Standard Deviation For {}'.format(title_var))
    # display ACF
    plot_acf(data)
    plt.show()


def time_series(data, regression_type, data_start_date, data_months_amount, predict_start_date,
                predict_months, data_title, forecast_title):

    # data start: yyyy-mm-dd  start: "2014-01-01" / predict: "2015-11-01"
    # data_months_amount: 22
    # predict months: 4


    # DATA ADJUSTMENT
    start = datetime.datetime.strptime(data_start_date, "%Y-%m-%d")
    date_list = [start + relativedelta(months=x) for x in range(0, data_months_amount)] #
    data['index'] = date_list
    data.set_index(['index'], inplace=True)
    data.index.name = None

    data.columns = [data_title]

    if regression_type == "ARMA":
        mod = sm.tsa.statespace.SARIMAX(data, trend='n', order=(1, 0, 1))
    elif regression_type == "ARIMA":
        mod = sm.tsa.statespace.SARIMAX(data, trend='n', order=(1, 1, 1))
    if regression_type == "SARIMA":
        # SARIMA for seasonal        auto-regression / iteration / moving-averages -> again but with seasonal
        mod = sm.tsa.statespace.SARIMAX(data, trend='n', order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = mod.fit()

    # MAKE FUTURE PREDICTIONS
    # start predicting from:
    start = datetime.datetime.strptime(predict_start_date, "%Y-%m-%d")
    # create amount of months
    date_list = [start + relativedelta(months=x) for x in range(0, predict_months)]
    # future months
    future = pd.DataFrame(index=date_list, columns=data.columns)
    # concat the df with future dates (future dates don't have value yet)
    df = pd.concat([data, future])

    # start= future row number start -> end
    df[forecast_title] = results.predict(start=22, end=24, dynamic=True)
    # plot only last 24 entries (12 existing / future)
    df[[data_title, forecast_title]].iloc[-26:].plot()

    plt.show()



