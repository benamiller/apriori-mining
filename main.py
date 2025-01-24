filename = "A-NUHa0sQ1C0nBpyRUTG5g_3260c54dad114a1a96af95bf746f9df1_categories.txt"

items = []

with open(filename, 'r') as file:
    for line in file:
        words = line.strip().split(";")
        items.extend(words)

    print(items[:10])


