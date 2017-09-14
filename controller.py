from config import NUM_LIST, IS_SAMPLE, EQUATION

from equations.box_plot import BoxPlot
from equations.iqr import IQR
from equations.mean import Mean
from equations.median import Median
from equations.outliers import Outliers
from equations.standard_deviation import StandardDeviation
from equations.variance import Variance


class Controller(object):
    def __init__(self):
        super(Controller, self).__init__()

        self._equation_set = {'box_plot', 'iqr', 'mean', 'median', 'outliers', 'standard_deviation', 'variance'}

    def solve_equation(self, equation, st_list, sample=False):
        if equation not in self._equation_set:
            raise ValueError('Equation not available. Please choose from the following list: \n\t{}'.format(
                self._equation_set
            ))

        if equation == 'box_plot':
            result = BoxPlot.get_box_plot(st_list)

        elif equation == 'iqr':
            result = IQR.create_iqr(st_list)

        elif equation =='mean':
            result = Mean.get_mean(st_list)

        elif equation == 'median':
            result = Median.get_median(st_list)

        elif equation == 'outliers':
            result = Outliers.create_outliers(st_list)

        elif equation == 'standard_deviation':
            result = StandardDeviation.get_standard_deviation(st_list, sample)

        elif equation == 'variance':
            result = Variance.get_variance(st_list, sample)


if __name__ == '__main__':
    controller = Controller()

    equation = EQUATION
    st_list = NUM_LIST
    sample = IS_SAMPLE

    result = controller.solve_equation(equation=equation, st_list=st_list, sample=sample)


