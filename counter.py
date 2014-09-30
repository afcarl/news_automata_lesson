# simple word counter
def count_words(doc):
    counts = {}
    words = doc.split(' ')

    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    return counts
