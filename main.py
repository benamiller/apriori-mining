from itertools import combinations
from collections import defaultdict

filename = "A-NUHa0sQ1C0nBpyRUTG5g_3260c54dad114a1a96af95bf746f9df1_categories.txt"
part1 = "part1.txt"
part2 = "part2.txt"

MIN_SUPPORT = 771

items = []
item_to_support = {}
transactions = []

with open(filename, 'r') as file:
    for line in file:
        words = line.strip().split(";")
        transactions.append(words)
        items.extend(words)

        for word in words:
            if word in item_to_support:
                item_to_support[word] += 1
            else:
                item_to_support[word] = 1

    print(items[:10])
    print(item_to_support['Shopping'])
    print(item_to_support['Restaurants'])
    print(min(item_to_support.values()))
    print(max(item_to_support.values()))

with open(part1, 'w') as file:
    for item, support in item_to_support.items():
        if support > MIN_SUPPORT:
            file.write(f"{support}:{item}\n")

frequent_itemsets = []
frequent_itemsets.append({frozenset([item]) for item, support in item_to_support.items() if support > MIN_SUPPORT})
itemset_supports = {1: {frozenset([item]): support for item, support in item_to_support.items() if support > MIN_SUPPORT}}
print(frequent_itemsets)

k = 2
while True:
    candidate_itemsets = set(
        [frozenset(set1.union(set2)) for set1 in frequent_itemsets[-1] for set2 in frequent_itemsets[-1] if len(set1.union(set2)) == k]
    )

    candidate_supports = defaultdict(int)

    for transaction in transactions:
        transaction_set = set(transaction)
        for candidate in candidate_itemsets:
            if set(candidate).issubset(transaction_set):
                candidate_supports[candidate] += 1

    current_frequent_itemsets = {
            candidate for candidate, support in candidate_supports.items() if support > MIN_SUPPORT
    }

    itemset_supports[k] = {
            candidate: support for candidate, support in candidate_supports.items() if support > MIN_SUPPORT
    }

    if not current_frequent_itemsets:
        break

    frequent_itemsets.append(current_frequent_itemsets)
    k += 1

with open(part2, 'w') as file:
    for length, itemsets in itemset_supports.items():
        for itemset, support in itemsets.items():
            file.write(f"{support}:{';'.join(itemset)}\n")
    

