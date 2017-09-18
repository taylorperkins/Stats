import sys

from math import floor

from config.args import NUM_LIST
from config.exceptions import NotFoundException


class Percentile(object):

    @staticmethod
    def get_percentile(st_list, **kwargs):
        """Returns either the percentile, or the given bucket for a percentile of a given dataset"""
        print_results = kwargs.get('print_results')

        amount = kwargs.get('amount')
        include_amount = kwargs.get('include_amount')

        # This is saying we are finding the amount BY percent.
        percent = kwargs.get('percent')

        if not amount:
            raise ValueError('get_percentile must have an amount to look for')

        dataset_length = len(st_list)

        if percent:
            result = Percentile.get_amount(st_list, amount, dataset_length)
        else:
            result = Percentile.get_percentage(st_list, amount, dataset_length, include_amount=include_amount)

        if print_results:
            return Percentile.print_results(result)

        return st_mean

    @staticmethod
    def get_percentage(st_list, amount, dataset_length, include_amount=False):

        try:
            amount_index = st_list.index(amount)
        except Exception:
            raise NotFoundException('{} does not appear to be in your dataset.'.format(amount))

        if not include_amount:
            percentile = amount_index / dataset_length

        else:
            next_amount_index = 0
            for ind in range(amount_index, dataset_length):
                if ind == dataset_length - 1:
                    next_amount_index = ind + 1
                elif st_list[ind] is not amount:
                    next_amount_index = ind
                    break

            percentile = next_amount_index / dataset_length

        return percentile

    @staticmethod
    def get_amount(st_list, amount, dataset_length):

        ind = floor(amount * dataset_length)

        return st_list[ind]

    @staticmethod
    def print_results(st_mean):
        result_string = str()

        result_string += "Here is your percentile: {}".format(st_mean)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    mean = Percentile.get_percentile(st_list, print_results=True)

    print(mean)
