from collections import defaultdict
import concurrent.futures
from typing import List, Tuple, Dict
from src.functions.helpers import preprocess_text


def map_function(chunk: str) -> List[Tuple[str, int]]:
    words = chunk.split()
    return [(word, 1) for word in words if len(word) > 1]


def shuffle_function(mapped_values: List[Tuple[str, int]]) -> Dict[str, List[int]]:
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return dict(shuffled)


def reduce_function(shuffled_values: Dict[str, List[int]]) -> Dict[str, int]:
    reduced = {}
    for key, values in shuffled_values.items():
        reduced[key] = sum(values)
    return reduced


def parallel_map_reduce(input_text: str, num_workers: int = 4) -> Dict[str, int]:
    processed_text = preprocess_text(input_text)

    words = processed_text.split()
    chunk_size = max(1, len(words) // num_workers)
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    mapped_values = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        map_results = list(executor.map(map_function, chunks))
        for result in map_results:
            mapped_values.extend(result)

    shuffled_values = shuffle_function(mapped_values)

    reduced_values = reduce_function(shuffled_values)

    return reduced_values