import sys

from config import NUM_LIST


class Mean(object):

    @staticmethod
    def get_mean(st_list, print_results=False):
        st_mean = sum(st_list) / len(st_list)

        if print_results:
            return Mean.print_results(st_mean)

        return st_mean

    @staticmethod
    def print_results(st_mean):
        result_string = str()

        result_string += "Here is your mean: {}".format(st_mean)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    mean = Mean.get_mean(st_list, print_results=True)

    print(mean)
