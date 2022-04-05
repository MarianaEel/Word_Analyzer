# import library
import operator

# import other file
from module import file_reader
from module import plotter


def word_analyzer(fname):
    NLTK_list = file_reader.file_reader("NLTK.txt")

    # scan file and add to word_list
    word_list = file_reader.file_reader(fname)

    # use word_dict
    word_dict = dict()
    for word in word_list:
        if(word.lower() in NLTK_list):
            continue
        elif (word_dict.get(word) is None):
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_word_list = list(
        reversed(sorted(word_dict.items(), key=operator.itemgetter(1))))

    # start plotting histogram
    plotter.plot(sorted_word_list)


if __name__ == '__main__':
    word_analyzer("../test/test_input/input.txt")
    word_analyzer("../test/test_input/Spring-2022-MS-Course-Offerings.pdf")
