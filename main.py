filename = "A-NUHa0sQ1C0nBpyRUTG5g_3260c54dad114a1a96af95bf746f9df1_categories.txt"
part1 = "part1.txt"
part2 = "part2.txt"

MIN_SUPPORT = 771

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

with open(part1, 'w') as file:
    for item, support in item_to_support.items():
        if support > MIN_SUPPORT:
            file.write(f"{support}:{item}\n")

with open(part2, 'w') as file:
    for item, support
    

