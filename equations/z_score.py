import sys
from math import sqrt

from config.args import NUM_LIST, VALUE, STANDARD_DEVIATION
from config.kwargs import MEAN

from equations.mean import Mean


class ZScore(object):

    @staticmethod
    def get_zscore(st_list, value, standard_deviation, **kwargs):
        print_results = kwargs.get('print_results')
        mean = kwargs.get('mean')

        if not mean:
            mean = Mean.get_mean(st_list)

        z_score = (value - mean) / standard_deviation

        if print_results:
            return ZScore.print_results(z_score)

        return z_score

    @staticmethod
    def print_results(z_score):
        result_string = str()

        result_string += "Here is your z-score: {}".format(z_score)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST
    value = VALUE
    mean = MEAN
    sd = STANDARD_DEVIATION

    z_score =  ZScore.get_zscore(st_list, value, standard_deviation, mean=mean, print_results=True)

    print(st_list_sd)
