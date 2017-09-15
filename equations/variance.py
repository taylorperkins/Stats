import sys

from config import NUM_LIST, IS_SAMPLE

from equations.mean import Mean
from equations.utils import to_bool


class Variance(object):

    @staticmethod
    def get_variance(st_list, **kwargs):
        sample = kwargs.get('sample')
        print_results = kwargs.get('print_results')

        st_mean = Mean.get_mean(st_list)

        squares_list = list()
        for num in st_list:
            squares_list.append((num - st_mean)**2)

        if not to_bool(sample):
            variance = sum(squares_list) / len(st_list)

        else:
            variance = sum(squares_list) / (len(st_list) - 1)

        if print_results:
            return Variance.print_results(variance)

        return variance

    @staticmethod
    def print_results(variance):
        result_string = str()

        result_string += "Here is your variance: {}".format(variance)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    sample = IS_SAMPLE
    st_list = NUM_LIST

    variance = Variance.get_variance(st_list, sample=sample, print_results=True)

    print(variance)
