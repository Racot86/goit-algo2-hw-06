import matplotlib.pyplot as plt
from typing import Dict

def visualize_top_words(word_frequency: Dict[str, int], top_n: int = 10) -> None:
    top_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:top_n]

    words, counts = zip(*top_words)

    plt.figure(figsize=(10, 8))
    plt.barh(words, counts, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title(f'Top {top_n} Words by Frequency')
    plt.gca().invert_yaxis()

    for i, count in enumerate(counts):
        plt.text(count, i, str(count), va='center')

    plt.tight_layout()
    plt.show()
