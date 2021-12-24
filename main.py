
from Descriptive import *


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

# # Cleaning the results
# rules_filtered = rules[['antecedents', 'consequents', 'lift']]
# print(rules_filtered)

# Filtering the results
# consequents = High Crime
rules_filtered = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
crime_rules = rules_filtered[rules_filtered.consequents == {'High-Robbery'}]
print(crime_rules)