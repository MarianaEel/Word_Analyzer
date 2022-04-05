import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot(sorted_word_list):
    # start plotting histogram
    word_frame = pd.DataFrame(sorted_word_list, columns=['Word', 'Times'])
    # print(word_frame)
    sns.barplot(data=word_frame.head(5), x="Word",
                y="Times", palette="coolwarm")
    plt.show()
