filename = "A-NUHa0sQ1C0nBpyRUTG5g_3260c54dad114a1a96af95bf746f9df1_categories.txt"

items = []
item_to_frequency = {}

with open(filename, 'r') as file:
    for line in file:
        words = line.strip().split(";")
        items.extend(words)

        for word in words:
            if word in item_to_frequency:
                item_to_frequency[word] += 1
            else:
                item_to_frequency[word] = 1

    print(items[:10])
    print(item_to_frequency['Shopping'])
    print(item_to_frequency['Restaurants'])
    print(min(item_to_frequency.values()))
    print(max(item_to_frequency.values()))


