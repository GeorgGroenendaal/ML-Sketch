from typing import List, Tuple
import numpy as np
from IPython.display import clear_output


def create_window(input_data: np.array, window_size: int) -> np.array:
    data_len = len(input_data)
    result = np.zeros((data_len-window_size+1, window_size, *input_data.shape[1:]))
    for i in range(data_len):
        if i+window_size <= data_len:
            result[i] = input_data[i:i+window_size]
    return result


def create_window_on_multiple_samples(input_data: np.array, window_size: int) -> np.array:
    """
    Similar to create_window, but now can take multiple samples, will output in one
    giant windowed np.array.
    """
    windowed_data = []
    for i, sample in enumerate(input_data):
        windowed_data.append(create_window(sample, window_size))

        if i % 10000 == 0:
            print(f"Now at {i}")
            clear_output(wait=True)
    result = np.concatenate(windowed_data)
    print(f"Done processing {i} samples, total of {result.shape[0]} windows and {result.shape[0] * result.shape[1]} datapoints")
    return np.concatenate(windowed_data)


def split_train_test(input_data: List) -> Tuple[np.array, np.array]:
    return input_data[:,0:-1], input_data[:,-1]