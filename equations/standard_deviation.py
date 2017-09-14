import sys
from math import sqrt

from config import NUM_LIST, IS_SAMPLE

from variance import Variance


class StandardDeviation(object):    

    @staticmethod
    def get_standard_deviation(st_list, sample=False, print_results=False):
        st_list_sd = sqrt(Variance.get_variance(st_list=st_list, sample=sample))

        if print_results:
            return StandardDeviation.print_results(st_list_sd)

        return st_list_sd

    @staticmethod
    def print_results(st_list_sd):
        result_string = str()

        result_string += "Here is your standard deviation: {}".format(st_list_sd)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    sample = IS_SAMPLE
    st_list = NUM_LIST

    st_list_sd =  StandardDeviation.get_standard_deviation(st_list, sample=sample, print_results=True)

    print(st_list_sd)
