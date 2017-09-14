import sys

from config import NUM_LIST

from median import Median


class BoxPlot(object):

    @staticmethod
    def get_halves(middle_indices, st_list):
        if len(middle_indices) > 1:
            first_half = st_list[:middle_indices[1]]
            second_half = st_list[middle_indices[1]:]

        else:
            first_half = st_list[:middle_indices[0]]
            second_half = st_list[middle_indices[0] + 1:]

        return first_half, second_half

    @staticmethod
    def get_box_plot(st_list):
        median = Median.get_median(st_list)

        middle_indices = Median.get_middle_indices(st_list)

        first_half, second_half = BoxPlot.get_halves(middle_indices, st_list)

        first_half_median = Median.get_median(first_half)
        second_half_median = Median.get_median(second_half)

        return {
            'median': median,
            'first_half_median': first_half_median,
            'second_half_median': second_half_median,
            'start': st_list[0],
            'end': st_list[-1]
        }


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    box_plot = BoxPlot.get_box_plot(st_list=st_list)

    print("Now finding sides in {}..\nHere is your list: \n\t{}".format(file_name, st_list))
    print("\nHere is your median: \n\t{}".format(box_plot.get('median')))
    print("Here is your first half median: \n\t{}".format(box_plot.get('first_half_median')))
    print("Here is your second half median: \n\t{}".format(box_plot.get('second_half_median')))
    print("Here is your start: \n\t{}".format(box_plot.get('start')))
    print("Here is your end: \n\t{}".format(box_plot.get('end')))