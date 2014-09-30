def flip_words(doc, mappings):
    for from_word, to_word in mappings.items():
        doc = doc.replace(from_word, to_word)
    return doc
