from typing import List, Tuple
import numpy as np

def create_window(input_data: List, step_size: int) -> np.array:
    data_len = len(input_data)
    result = np.zeros((data_len-step_size+1, step_size))
    for i in range(data_len):
        if i+step_size <= data_len:
            result[i] = input_data[i:i+step_size]
    return result


def split_train_test(input_data: List) -> Tuple[np.array, np.array]:
    return input_data[:,0:-1], input_data[:,-1].reshape((input_data.shape[0], 1))