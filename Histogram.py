import re
import random

source_text = open('book.txt').read().split()

histogram = {}  # create dict for histogram


def histogram_fun(source_text):  # create histogram to count freq in text
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
    return histogram


def cumulative_distribution(histogram):  # create tuple list from cum_dist
    distribution_list = []
    distribution_range = 0
    for distribution_word, freq in histogram.items():
        if distribution_word not in distribution_list:
            upper_limit = distribution_range + freq
            distribution_range += freq
            distribution_list.append((distribution_word, upper_limit))
    return distribution_list


def sample_from_cum(distribution_list):  # pull words from cumalative list
    token_tuple = distribution_list[-1]
    tokens = token_tuple[-1]
    index = random.randint(0, tokens - 1)  # the index is set here for true randomness
    for sample_word, upper_limit in distribution_list:
        if index < upper_limit:
            return sample_word  #run this a 1000 times, put the output into a
            # new list and run this into the same histogram and compare it


# def true_randomness(tokens):
#     sentence_list = []
#     for random_words in sentence_list:
#

def unique_words(histogram_fun):  # returns the total # of uinque words in data
    return len(histogram)


def frequency(word, histogram_fun):  # returns frequency of word in source text
    return histogram[word]


if __name__ == '__main__':
    x = cumulative_distribution(histogram_fun(source_text))
    print(sample_from_cum(x))
