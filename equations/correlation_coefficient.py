import sys

from config.args import XY_DATASET

from equations.mean import Mean
from equations.standard_deviation import StandardDeviation
from equations.z_score import ZScore


def get_xy_datasets(xy_dataset):
    x_dataset = [xy_tuple[0] for xy_tuple in xy_dataset]
    y_dataset = [xy_tuple[1] for xy_tuple in xy_dataset]

    return x_dataset, y_dataset


class CorrelationCoefficient(object):
    """
        A number between -1 and +1 calculated so as to represent the
        linear dependence of two variables or sets of data.
    """

    @staticmethod
    def get_correlation_coefficient(xy_dataset, **kwargs):
        print_results = kwargs.get('print_results')
        is_sample = kwargs.get('is_sample')

        ds_len = len(xy_dataset)
        if is_sample:
            ds_len = ds_len - 1

        xy_zscores_sum = CorrelationCoefficient.get_xy_zscore_sums(xy_dataset, is_sample)

        r = (1 / ds_len) * xy_zscores_sum

        if print_results:
            return CorrelationCoefficient.print_results(r)

        return r

    @staticmethod
    def get_xy_zscore_sums(xy_dataset, is_sample):
        x_dataset, y_dataset = get_xy_datasets(xy_dataset)

        x_mean = Mean.get_mean(x_dataset)
        y_mean = Mean.get_mean(y_dataset)

        x_standard_deviation = StandardDeviation.get_standard_deviation(x_dataset, sample=is_sample)
        y_standard_deviation = StandardDeviation.get_standard_deviation(y_dataset, sample=is_sample)

        xy_zscores = list()
        for xy_point in xy_dataset:
            x = xy_point[0]
            y = xy_point[1]

            x_zscore = ZScore.get_zscore(x_dataset, x, x_standard_deviation, mean=x_mean)
            y_zscore = ZScore.get_zscore(y_dataset, y, y_standard_deviation, mean=y_mean)

            xy_zscores.append(x_zscore * y_zscore)

        return sum(xy_zscores)

    @staticmethod
    def print_results(r):
        result_string = str()

        result_string += "Here is your correlation Coefficienc: \t{}".format(r)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    r = CorrelationCoefficient.get_correlation_coefficient(xy_dataset=xy_dataset, print_results=True)

    print(r)
