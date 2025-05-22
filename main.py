from src.functions.helpers import download_text
from src.functions.map_reduce import parallel_map_reduce
from src.functions.visualization import visualize_top_words


if __name__ == '__main__':
    url = "https://gutenberg.net.au/ebooks02/0200161h.html"

    print("Downloading text...")
    text = download_text(url)

    if text:
        print("Processing text...")
        word_counts = parallel_map_reduce(text)

        print("Visualizing results...")
        visualize_top_words(word_counts)

        print(f"Total unique words: {len(word_counts)}")
    else:
        print("Failed to download text. Please check the URL and try again.")
