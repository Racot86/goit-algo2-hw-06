# MapReduce Word Frequency Analyzer

This project implements a MapReduce paradigm to analyze word frequency in text downloaded from a URL. It demonstrates parallel processing techniques to efficiently process large texts and visualizes the most common words.

## Project Overview

The application:
1. Downloads text from a specified URL
2. Preprocesses the text (removes HTML tags, punctuation, and converts to lowercase)
3. Uses a MapReduce approach with parallel processing to count word frequencies
4. Visualizes the top most frequent words in a horizontal bar chart

## Project Structure

```
goit-algo2-hw-06/
├── main.py                      # Main application entry point
├── src/
│   └── functions/
│       ├── helpers.py           # Utility functions for downloading and preprocessing text
│       ├── map_reduce.py        # MapReduce implementation with parallel processing
│       └── visualization.py     # Functions for visualizing word frequency results
```

## How MapReduce Works in This Project

The MapReduce implementation follows these steps:

1. **Map Phase**: The text is split into chunks and processed in parallel. Each chunk is processed by the `map_function`, which splits the text into words and emits (word, 1) pairs.

2. **Shuffle Phase**: The `shuffle_function` groups all values by their keys (words), creating a dictionary where each key is a word and the value is a list of counts.

3. **Reduce Phase**: The `reduce_function` sums up all counts for each word, producing the final word frequency dictionary.

4. **Parallel Processing**: The implementation uses Python's `concurrent.futures.ThreadPoolExecutor` to parallelize the Map phase, improving performance for large texts.

## Dependencies

- Python 3.6+
- requests (for downloading text)
- matplotlib (for visualization)
- re (for text preprocessing)
- concurrent.futures (for parallel processing)

## How to Run

1. Ensure you have all dependencies installed:
   ```
   pip install requests matplotlib
   ```

2. Run the main script:
   ```
   python main.py
   ```

3. By default, the script downloads text from "https://gutenberg.net.au/ebooks02/0200161h.html". You can modify the URL in the main.py file.

## Example Output

The script will:
1. Print progress messages during execution
2. Display a horizontal bar chart showing the top 10 most frequent words
3. Print the total number of unique words found in the text

The visualization will look similar to this:

```
Top 10 Words by Frequency
--------------------------
the  |████████████████| 4532
and  |████████| 2345
of   |███████| 2100
to   |██████| 1876
a    |█████| 1543
in   |████| 1234
that |███| 987
was  |███| 876
he   |██| 765
it   |██| 654
```

## Performance Considerations

- The parallel processing approach significantly improves performance for large texts
- The number of workers can be adjusted in the `parallel_map_reduce` function (default is 4)
- For very large texts, memory usage should be monitored