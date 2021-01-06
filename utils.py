from typing import List, Tuple

import numpy as np
import svgwrite
from IPython.display import SVG, clear_output, display
from six.moves import xrange  # type: ignore


def create_window(input_data: np.array, window_size: int) -> np.array:
    data_len = len(input_data)
    result = np.zeros((data_len - window_size + 1, window_size, *input_data.shape[1:]))
    for i in range(data_len):
        if i + window_size <= data_len:
            result[i] = input_data[i : i + window_size]
    return result


def create_window_on_multiple_samples(
    input_data: np.array, window_size: int
) -> np.array:
    """
    Similar to create_window, but now can take multiple samples, will output in one
    giant windowed np.array.
    """
    windowed_data = []
    i = 0
    for i, sample in enumerate(input_data):
        windowed_data.append(create_window(sample, window_size))

        if i % 10000 == 0:
            print(f"Now at {i}")
            clear_output(wait=True)
    result = np.concatenate(windowed_data)
    print(
        f"Done processing {i} samples, total of {result.shape[0]} windows and {result.shape[0] * result.shape[1]} datapoints"
    )
    return result


def split_train_test(input_data: List) -> Tuple[np.array, np.array]:
    return input_data[:, 0:-1], input_data[:, -1]


# helper function for draw_strokes
def get_bounds(data, factor):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    abs_x = 0
    abs_y = 0
    for i in xrange(len(data)):
        x = float(data[i, 0]) / factor
        y = float(data[i, 1]) / factor
        abs_x += x
        abs_y += y
        min_x = min(min_x, abs_x)
        min_y = min(min_y, abs_y)
        max_x = max(max_x, abs_x)
        max_y = max(max_y, abs_y)

    return (min_x, max_x, min_y, max_y)


# little function that displays vector images and saves them to .svg
def draw_strokes(data, factor=2, svg_filename="sample.svg"):
    min_x, max_x, min_y, max_y = get_bounds(data, factor)
    dims = (50 + max_x - min_x, 50 + max_y - min_y)
    dwg = svgwrite.Drawing(svg_filename, size=dims)
    dwg.add(dwg.rect(insert=(0, 0), size=dims, fill="white"))
    lift_pen = 1
    abs_x = 25 - min_x
    abs_y = 25 - min_y
    p = "M%s,%s " % (abs_x, abs_y)
    command = "m"
    for i in xrange(0, 20):
        if lift_pen == 1:
            command = "m"
        elif command != "l":
            command = "l"
        else:
            command = ""
        x = float(data[i, 0]) / factor
        y = float(data[i, 1]) / factor
        lift_pen = data[i, 2]
        p += command + str(x) + "," + str(y) + " "
    the_color = "red"
    stroke_width = 2
    dwg.add(dwg.path(p).stroke(the_color, stroke_width).fill("none"))
    for i in xrange(20, len(data)):
        if lift_pen == 1:
            command = "m"
        elif command != "l":
            command = "l"
        else:
            command = ""
        x = float(data[i, 0]) / factor
        y = float(data[i, 1]) / factor
        lift_pen = data[i, 2]
        p += command + str(x) + "," + str(y) + " "
    the_color = "black"
    stroke_width = 1
    dwg.add(dwg.path(p).stroke(the_color, stroke_width).fill("none"))
    dwg.save()
    display(SVG(dwg.tostring()))


# generate a 2D grid of many vector drawings
def make_grid_svg(s_list, grid_space=10.0, grid_space_x=15.0):
    def get_start_and_end(x):
        x = np.array(x)
        x = x[:, 0:2]
        x_start = x[0]
        x_end = x.sum(axis=0)
        x = x.cumsum(axis=0)
        x_max = x.max(axis=0)
        x_min = x.min(axis=0)
        center_loc = (x_max + x_min) * 0.5
        return x_start - center_loc, x_end

    x_pos = 0.0
    y_pos = 0.0
    result = [[x_pos, y_pos, 1]]
    for sample in s_list:
        s = sample[0]
        grid_loc = sample[1]
        grid_y = grid_loc[0] * grid_space + grid_space * 0.5
        grid_x = grid_loc[1] * grid_space_x + grid_space_x * 0.5
        start_loc, delta_pos = get_start_and_end(s)

        loc_x = start_loc[0]
        loc_y = start_loc[1]
        new_x_pos = grid_x + loc_x
        new_y_pos = grid_y + loc_y
        result.append([new_x_pos - x_pos, new_y_pos - y_pos, 0])

        result += s.tolist()
        result[-1][2] = 1
        x_pos = new_x_pos + delta_pos[0]
        y_pos = new_y_pos + delta_pos[1]
    return np.array(result)
