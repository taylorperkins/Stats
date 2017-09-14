import sys
from mean import Mean

from config import NUM_LIST, IS_SAMPLE

from utils import to_bool


class Variance(object):

    @staticmethod
    def get_variance(st_list, sample=False):
        st_mean = Mean.get_mean(st_list)

        squares_list = list()
        for num in st_list:
            squares_list.append((num - st_mean)**2)

        if not to_bool(sample):
            return sum(squares_list) / len(st_list)

        return sum(squares_list) / (len(st_list) - 1)


if __name__ == '__main__':
    file_name = sys.argv[0]
    sample = IS_SAMPLE
    st_list = NUM_LIST

    print("Now finding variance in {}..\nHere is your list: \n\t{}".format(file_name, st_list))
    print("\nHere is your variance: {}".format(Variance.get_variance(st_list, sample=sample)))

