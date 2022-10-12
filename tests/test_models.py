"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_integer():
    """Test that the max function works for an array of positive integers."""
    from inflammation.models import daily_max

    test_input = ([[1, 2],
                   [3, 4],
                   [5, 6]])
    test_result = np.array([5, 6])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_zeros():
    """Test that the max funciton works for an array of zeros."""
    from inflammation.models import daily_max
    
    test_input = ([[0, 0],
                   [0, 0],
                   [0, 0]])
    test_result = np.array([0, 0])

    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min_integer():
    """Test that the max function works for an array of positive integers."""
    from inflammation.models import daily_min

    test_input = ([[1, 2],
                   [3, 4],
                   [5, 6]])
    test_result = np.array([1, 2])

    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_zeros():
    """Test that the max funciton works for an array of zeros."""
    from inflammation.models import daily_min
    
    test_input = ([[0, 0],
                   [0, 0],
                   [0, 0]])
    test_result = np.array([0, 0])

    npt.assert_array_equal(daily_min(test_input), test_result)