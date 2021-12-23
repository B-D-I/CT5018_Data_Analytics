import statistics

import Data_Variables
from Time_Series_Functions import *
from Hypothesis import *



sales_figs, axes = plt.subplots(1, 3, sharey=True)

regression_data.plot(kind='scatter', x='Employment', y='Robbery', ax=axes[0], figsize=(16, 8))
regression_data.plot(kind='scatter', x='Unemployment', y='Robbery', ax=axes[1])
regression_data.plot(kind='scatter', x='Income', y='Robbery', ax=axes[2])

#plt.show()

# lrm = smf.ols(formula='Robbery ~ Employment', data=regression_data).fit()
#
# print(lrm.params)

# # testing the model
# X_test_new = pd.DataFrame({'unemployment': [1000]})   # for every 1000 per 100k unemployed, get x crime
# print(X_test_new)
# prediction = lrm.predict(X_test_new)
# print(prediction)

# robss = [0.674, 0.893, 0.869, 0.729]
# print(statistics.mean(robss))

# P -VALUES
# print(lrm.pvalues)



# MULTIPLE LINEAR REGRESSION

feature_cols = ['Unemployment', 'Employment']

X = regression_data[feature_cols]
Y = regression_data.Robbery

lr_model = LinearRegression()
lr_model.fit(X, Y)

print(lr_model.intercept_)  # B0   - if no change in employment, unemployment, income - this is crime amount
print(lr_model.coef_)   # B1, B2, B3 - employment and income decrease as crime increases, unemployment increas wth crime

# testing the model
X_test_new = pd.DataFrame({'Unemployment': [3419], 'Employment': [81195]})
print(X_test_new)
prediction = lr_model.predict(X_test_new)
print(prediction)   # if all feature cols increase this will be the crime amount
