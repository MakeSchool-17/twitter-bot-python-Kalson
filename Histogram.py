import re

source_text = open('fish.txt').read().split()

histogram = {}  # create dict


def histogram_fun(source_text):
    for word in source_text:
        if word not in histogram:
            new_word = re.sub(r"\W+", "", word)
            new_word = new_word.lstrip('_')
            new_word = new_word.rstrip('_')
            histogram[new_word] = 1
        else:
            new_word = re.sub(r"\W+", "", word)
            new_word = new_word.lstrip('_')
            new_word = new_word.rstrip('_')
            histogram[new_word] += 1
    # tokens = sum(histo.values())
    return histogram


def cumulative_distribution(histogram):
    distribution_list = []
    distribution_range = 0
    for x, freq in histogram.items():
        if x not in distribution_list:
            upper_limit = distribution_range + freq
            distribution_range += freq
            distribution_list.append((x, upper_limit))
    return distribution_list


def unique_words(histogram_fun):  # returns the total # of uinque words in data
    return len(histogram)


def frequency(word, histogram_fun):  # returns frequency of word in source text
    return histogram[word]


if __name__ == '__main__':
    print(cumulative_distribution(histogram_fun(source_text)))
