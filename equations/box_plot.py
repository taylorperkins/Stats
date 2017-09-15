import sys

from config import NUM_LIST

from equations.median import Median


class BoxPlot(object):

    @staticmethod
    def get_box_plot(st_list, **kwargs):
        print_results = kwargs.get('print_results')

        median = Median.get_median(st_list)

        middle_indices = Median.get_middle_indices(st_list)

        first_half, second_half = BoxPlot.get_halves(middle_indices, st_list)

        first_half_median = Median.get_median(first_half)
        second_half_median = Median.get_median(second_half)

        box_plot = {
            'median': median,
            'first_half_median': first_half_median,
            'second_half_median': second_half_median,
            'start': st_list[0],
            'end': st_list[-1]
        }
        if print_results:
            return BoxPlot.print_results(box_plot)

        return box_plot

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
    def print_results(box_plot):
        result_string = str()

        result_string += """Here is your median: \t\t\t\t{}
        \rHere is your first half median: \t{}
        \rHere is your second half median: \t{}
        \rHere is your start: \t\t\t\t{}
        \rHere is your end: \t\t\t\t\t{}
        """.format(
            box_plot.get('median'),
            box_plot.get('first_half_median'),
            box_plot.get('second_half_median'),
            box_plot.get('start'),
            box_plot.get('end')
        )

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    box_plot = BoxPlot.get_box_plot(st_list=st_list, print_results=True)

    print(box_plot)