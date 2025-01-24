filename = "A-NUHa0sQ1C0nBpyRUTG5g_3260c54dad114a1a96af95bf746f9df1_categories.txt"

items = []
item_to_support = {}

with open(filename, 'r') as file:
    for line in file:
        words = line.strip().split(";")
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

for item, support in item_to_support.items():

