
from Functions import *

# Classification
# Y = encoded_data.iloc[:,7]
# X = encoded_data.iloc[:,0:7]
# X.columns = ['Unemployment', 'Employment', "Income", "Burglary", "Robbery", "Theft", "Combined"]
#
# model = GaussianNB()
# model.fit(X, Y)
# prediction_test = [1, 2, 2, 2, 2, 2, 2]
# predicted_class = model.predict(np.reshape(prediction_test,[1,-1]))
# print("predicted class: ", predicted_class)


# Association Rules
print(encoded_data.head())
# Building the model
frq_items = apriori(encoded_data, min_support=0.1, use_colnames=True)
# Collecting the rules
rules = association_rules(frq_items, metric="lift", min_threshold=1)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
print(rules.head())

# Filtering the rules
print(rules[(rules['confidence'] > 0.85) & (rules['lift'] > 1.5)])

# Cleaning the results
rules_filtered = rules[['antecedents', 'consequents', 'lift']]
print(rules_filtered)

# Filtering the results
# consequents = High Combined Crime
rules_filtered = rules[['antecedents', 'consequents', 'support', 'confidence','lift']]
combined_crime_rules = rules_filtered[rules_filtered.consequents == {'High-Combined'}]
print(combined_crime_rules)