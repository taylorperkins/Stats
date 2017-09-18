from config.args import EQUATION, NUM_LIST
from config.kwargs import AMOUNT, INCLUDE_AMOUNT, IS_SAMPLE, MID_RANGE, PERCENT, PRINT_RESULTS
from config.exceptions import NotFoundException

from equations.box_plot import BoxPlot
from equations.iqr import IQR
from equations.mad import MAD
from equations.mean import Mean
from equations.median import Median
from equations.outliers import Outliers
from equations.percentile import Percentile
from equations.range import Range
from equations.standard_deviation import StandardDeviation
from equations.variance import Variance


class Controller(object):
    def __init__(self):
        super(Controller, self).__init__()

        self._equation_set = {'box_plot', 'iqr', 'mad', 'mean', 'median', 'outliers', 'percentile', 'range',
                              'standard_deviation', 'variance'}

    def solve_equation(self, equation, st_list, amount=False, include_amount=False, mid_range=False, percent=False,
                       sample=False, print_results=False):

        if equation not in self._equation_set:
            raise ValueError('Equation not available. Please choose from the following list: \n\t{}'.format(
                self._equation_set
            ))

        st_list = sorted(st_list, key=int)

        if equation == 'box_plot':
            result = BoxPlot.get_box_plot(st_list, print_results=print_results)

        elif equation == 'iqr':
            result = IQR.get_iqr(st_list, print_results=print_results)

        elif equation =='mad':
            result = MAD.get_mad(st_list, print_results=print_results)

        elif equation =='mean':
            result = Mean.get_mean(st_list, print_results=print_results)

        elif equation == 'median':
            result = Median.get_median(st_list, print_results=print_results)

        elif equation == 'outliers':
            result = Outliers.get_outliers(st_list, print_results=print_results)

        elif equation == 'percentile':
            result = Percentile.get_percentile(
                st_list, amount=amount, include_amount=include_amount, percent=percent, print_results=print_results)

        elif equation == 'range':
            result = Range.get_range(st_list, mid_range=mid_range, print_results=print_results)

        elif equation == 'standard_deviation':
            result = StandardDeviation.get_standard_deviation(st_list, sample=sample, print_results=print_results)

        elif equation == 'variance':
            result = Variance.get_variance(st_list, sample=sample, print_results=print_results)

        else:
            raise ValueError('Nope, can\'t do {}'.format(equation))

        return Controller.print_results(equation, result)

    @staticmethod
    def print_results(equation, result):
        results_string = """\nOk, printing your results for {}: \n\n{}""".format(equation, result)

        return results_string


if __name__ == '__main__':
    controller = Controller()

    result = controller.solve_equation(
        equation=EQUATION,
        st_list=NUM_LIST,
        amount=AMOUNT,
        include_amount=INCLUDE_AMOUNT,
        mid_range=MID_RANGE,
        percent=PERCENT,
        sample=IS_SAMPLE,
        print_results=PRINT_RESULTS
    )

    print(result)
