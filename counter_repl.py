from counter import count_words

doc = 'They sleep by the thousands on what are normally the busiest boulevards of this crammed, nonstop city. They live on crackers, bananas and bottled water. They clean up their trash, even taking the time to pick out plastic and paper for recycling. Their shield of choice, and the symbol of their cause, is the umbrella: protection against the sun, rain - and pepper spray fired by the riot police.'

print('\n~~ unsorted counts ~~\n')
counts = count_words(doc)
print(counts)

# sort it, but this is lowest to highest...
print('\n~~ sorted counts, ascending ~~\n')
counts_sorted = sorted(counts.items(), key=lambda x: x[1])
print(counts_sorted)

# so reverse it
print('\n~~ sorted counts, descending ~~\n')
counts_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print(counts_sorted)

# get the most common word
print('\n~~ most common word ~~\n')
print(counts_sorted[0])
