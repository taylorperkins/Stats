import sys

from config import NUM_LIST


class Mean(object):

    @staticmethod
    def get_mean(st_list):
        st_mean = sum(st_list) / len(st_list)
        return st_mean


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    print("Now finding mean in {}..\nHere is your list: \n\t{}".format(file_name, st_list))
    print("\nHere is your mean: {}".format(Mean.get_mean(st_list)))
