import sys

from config import NUM_LIST

from equations.box_plot import BoxPlot
from equations.iqr import IQR


class Outliers(object):

    @staticmethod
    def get_outliers(st_list, print_results=True):
        box_plot = BoxPlot.get_box_plot(st_list)

        iqr = IQR.create_iqr(box_plot)

        q1 = box_plot.get('first_half_median')
        q3 = box_plot.get('second_half_median')

        start = st_list[0]
        end = st_list[-1]

        outliers = Outliers.create_outliers(st_list, iqr, box_plot)

        if print_results:
            return Outliers.print_results(outliers)

        return outliers

    @staticmethod
    def create_outliers(st_list, iqr, box_plot):
        q1 = box_plot.get('first_half_median')
        q3 = box_plot.get('second_half_median')

        q1_outlier_point = q1 - (iqr * 1.5)
        q3_outlier_point = q3 + (iqr * 1.5)

        q1_outliers = list(filter(lambda x: x < q1_outlier_point, st_list))
        q3_outliers = list(filter(lambda x: x > q3_outlier_point, st_list))

        outliers = [
            {'placement': 'Q1 Outliers', 'outliers': q1_outliers},
            {'placement': 'Q3 Outliers', 'outliers': q3_outliers}
        ]

        return outliers

    @staticmethod
    def print_results(outliers):
        result_string = str()

        for outlier in outliers:
            if outlier['outliers']:
                result_string += """\nHere are your {}: {}\n""".format(
                    outlier['placement'], outlier['outliers'])

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    outliers = Outliers.get_outliers(st_list, print_results=True)

    print(outliers)

    # print("Now finding outliers in {}..\nHere is your list: \n\t{}".format(file_name, st_list))
    # for outlier in outliers:
    #     if outlier['outliers']:
    #         print("\nHere are your outliers for {}: \n\t{}".format(outlier['placement'], outlier['outliers']))

