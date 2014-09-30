def flip_words(doc, mappings):
    for from_word, to_word in mappings.items():
        doc = doc.replace(from_word, to_word)
    return doc


class Flipper():
    def __init__(self, mappings):
        self.mappings = mappings

    def flip(self, doc):
        return flip_words(doc, self.mappings)
