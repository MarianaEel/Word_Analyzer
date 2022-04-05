from PyPDF3 import PdfFileWriter, PdfFileReader
import string
import os


def file_reader(fname):
    my_path = os.path.abspath(os.path.dirname(__file__))
    fname = os.path.join(my_path, fname)
    word_list = []
    # PDF read
    if ".pdf" == fname[-4:]:
        print("read pdf file")
        with open(fname, 'rb') as f:
            if f:
                ipdf = PdfFileReader(f)
                lines = [p.extractText() for p in ipdf.pages]

    # txt read as default
    # if ".txt" == fname[-4:]:
    else:
        print("read txt file")
        f = open(fname, "r", encoding="utf-8")
        lines = f.readlines()

    for line in lines:
        for word in line.split():
            word = word.strip(string.whitespace)
            if word[-1] in ['.', ',', ':', '-', '_']:
                word = word[:-1]
                if word == '':
                    continue
            word_list.append(word)

    return word_list
