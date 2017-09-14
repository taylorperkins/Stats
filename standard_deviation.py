import sys
from math import sqrt

from config import NUM_LIST, IS_SAMPLE

from variance import Variance


class StandardDeviation(object):    

    @staticmethod
    def get_standard_deviation(st_list, sample=False):
        st_list_sd = sqrt(Variance.get_variance(st_list=st_list, sample=sample))

        return st_list_sd


if __name__ == '__main__':
    file_name = sys.argv[0]
    sample = IS_SAMPLE
    st_list = NUM_LIST

    print("Now finding standard deviation in {}..\nHere is your list: \n\t{}".format(file_name, st_list))
    print("\nHere is your standard deviation: {}".format(
        StandardDeviation.get_standard_deviation(st_list, sample=sample)))

