
import pytest

import project_module


def test_something(my_data):
    assert my_data == 42

@pytest.mark.parametrize("values,expected_results",[
    (
    [1,2,3,4,5,6],
    [2.0, 3.0, 4.0, 5.0],
    ),
    (
    [-1,-2,-3,-4,-5,-6],
    [-2.0, -3.0, -4.0 , -5.0], # Comarison value was missing
    ),
    (
    [-3,-5,-6,-4,-5,-78],
    [-2.0, -3.0, -4.0 , -5.0], # Added a failing case
    ),
])
def test_rolling_average(values,expected_results):

    result = project_module.rolling_average(values, 3)
    assert result == expected_results
