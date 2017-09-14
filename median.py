import sys

from config import NUM_LIST

from mean import Mean


class Median(object):

    @staticmethod
    def get_middle_indices(st_list):
        num_list_len = len(st_list)

        if num_list_len % 2 == 1:
            half_point = int((num_list_len - 1) / 2)
            middle_indices = [half_point]
        else:
            half_point = int((num_list_len) / 2)
            middle_indices = [half_point - 1, half_point]

        return middle_indices

    @staticmethod
    def get_median(st_list):
        middle_indices = Median.get_middle_indices(st_list)

        middle_ints = list()
        for ind in middle_indices:
            middle_ints.append(st_list[ind])

        median = Mean.get_mean(st_list=middle_ints)

        return median


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    print("Now finding median in {}..\nHere is your list: \n\t{}".format(file_name, st_list))
    print("\nHere is your median: {}".format(Median.get_median(st_list)))
