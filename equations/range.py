import sys

from config import NUM_LIST

from equations.mean import Mean


class Range(object):

    @staticmethod
    def get_range(st_list, mid_range=False, print_results=False):

        start = st_list[0]
        end = st_list[-1]

        range = end - start

        if mid_range:
            range = Mean.get_mean([start, end])

        if print_results:
            return Range.print_results(range)

        return range

    @staticmethod
    def print_results(range):
        result_string = str()

        result_string += "Here is your range: {}".format(range)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    range = Range.get_range(st_list=st_list)

    print(range)