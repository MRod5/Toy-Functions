"""


MRodriguez - 2020
"""

from fitness_tester import FitnessTester

qtest = FitnessTester('toboggan')

xi = qtest.x1boundary[0]
xf = qtest.x1boundary[1]

yi = qtest.x2boundary[1]
yf = qtest.x2boundary[1]

z = qtest.quality_function(0,0)

print(z)


qtest.quality_function_plotter()