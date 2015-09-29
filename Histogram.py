import re

source_text = open('book.txt').read().split()

histo = {}
def histogram(source_text):
    for word in source_text:
        if word not in histo:
            new_word = re.sub(r"\W+", "", word)
            new_word = new_word.lstrip('_')
            new_word = new_word.rstrip('_')
            histo[new_word] = 1
        else:
            new_word = re.sub(r"\W+", "", word)
            new_word = new_word.lstrip('_')
            new_word = new_word.rstrip('_')
            histo[new_word] += 1
    return histo

def unique_words(histogram):
    return len(histo)

def frequency(word, histogram):
    return histo[word]

if __name__ == '__main__':
    print(histogram(source_text))
