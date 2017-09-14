import sys

from config import NUM_LIST

from box_plot import BoxPlot
from median import Median


class IQR(object):

    @staticmethod
    def get_iqr(box_plot):
        first_half_median = box_plot.get('first_half_median')
        second_half_median = box_plot.get('second_half_median')

        return second_half_median - first_half_median

    @staticmethod
    def create_iqr(st_list):
        box_plot = BoxPlot.get_box_plot(st_list)

        iqr = IQR.get_iqr(box_plot)

        return iqr


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    iqr = IQR.create_iqr(st_list=st_list)

    print("Now finding inter-quartile range in {}..\nHere is your list: \n\t{}".format(file_name, st_list))
    print("\nHere is your IQR: \n\t{}".format(iqr))