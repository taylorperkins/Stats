import sys

from config.args import NUM_LIST

from equations.mean import Mean


class MAD(object):

    @staticmethod
    def get_mad(st_list, **kwargs):
        print_results = kwargs.get('print_results')

        st_mean = Mean.get_mean(st_list)

        grouped_distance = list()
        for num in st_list:
            grouped_distance.append(abs(num - st_mean))

        mad = Mean.get_mean(grouped_distance)

        if print_results:
            return MAD.print_results(mad)

        return st_mean

    @staticmethod
    def print_results(mad):
        result_string = str()

        result_string += "Here is your mean absolute deviation: {}".format(mad)

        return result_string


if __name__ == '__main__':
    file_name = sys.argv[0]
    st_list = NUM_LIST

    mean = Mean.get_mad(st_list, print_results=True)

    print(mean)
