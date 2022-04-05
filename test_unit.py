from module import file_reader
import word_analyzer


def test_file_reader():
    word_list = file_reader.file_reader("../test/test_input/input.txt")
    assert(word_list!=[])
    word_list = file_reader.file_reader(
        "../test/test_input/Spring-2022-MS-Course-Offerings.pdf")
    assert(word_list!=[])


def test_word_analyzer():
    word_analyzer.word_analyzer("../test/test_input/input.txt")
    word_analyzer.word_analyzer(
        "../test/test_input/Spring-2022-MS-Course-Offerings.pdf")


if __name__ == '__main__':
    test_file_reader()
    test_word_analyzer()
