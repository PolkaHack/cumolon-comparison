import matplotlib.pyplot as plt
from .comparator import FileComparison
import numpy as np


def plot_similarity_bar_chart(numbers: list[int], title: str, save_to_file_path: str = None):
    plt.figure()
    bins = np.arange(0, 101, 5)
    plt.hist(numbers, bins=bins)
    plt.title(title)
    plt.xlabel('File Similarity')
    plt.ylabel('Count')

    if save_to_file_path:
        plt.savefig(save_to_file_path)
    else:
        plt.show()
