# Sample dataset
data = [
    {'feature': 'Rain', 'outlook': 'Sunny', 'play': 'No'},
    {'feature': 'Rain', 'outlook': 'Overcast', 'play': 'Yes'},
    {'feature': 'Rain', 'outlook': 'Rainy', 'play': 'Yes'},
    {'feature': 'Sunny', 'outlook': 'Sunny', 'play': 'Yes'},
    {'feature': 'Sunny', 'outlook': 'Rainy', 'play': 'No'},
]

# Helper functions
import math

def calculate_entropy(data, target_attr):
    values = [record[target_attr] for record in data]
    frequencies = {val: values.count(val) for val in set(values)}
    entropy = sum(
        (-freq / len(values)) * math.log2(freq / len(values)) for freq in frequencies.values()
    )
    return entropy

def split_data(data, attribute, value):
    subset = [record for record in data if record[attribute] == value]
    return subset

def best_attribute(data, attributes, target_attr):
    base_entropy = calculate_entropy(data, target_attr)
    info_gains = {}

    for attribute in attributes:
        values = set(record[attribute] for record in data)
        subset_entropy = sum(
            (len(subset) / len(data)) * calculate_entropy(subset, target_attr)
            for val in values
            for subset in [split_data(data, attribute, val)]
        )
        info_gains[attribute] = base_entropy - subset_entropy

    return max(info_gains, key=info_gains.get)

# Recursive tree building
def build_tree(data, attributes, target_attr):
    # Base case: all labels are the same
    labels = [record[target_attr] for record in data]
    if len(set(labels)) == 1:
        return labels[0]

    # Base case: no more attributes
    if not attributes:
        return max(set(labels), key=labels.count)

    # Select best attribute
    best_attr = best_attribute(data, attributes, target_attr)
    tree = {best_attr: {}}

    # Recursive case: split data by the best attribute
    for value in set(record[best_attr] for record in data):
        subset = split_data(data, best_attr, value)
        subtree = build_tree(
            subset,
            [attr for attr in attributes if attr != best_attr],
            target_attr,
        )
        tree[best_attr][value] = subtree

    return tree

# Building the tree
attributes = ['feature', 'outlook']
target_attr = 'play'
decision_tree = build_tree(data, attributes, target_attr)

# Display the resulting tree
import pprint
pprint.pprint(decision_tree)
