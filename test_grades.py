
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades, 0) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades, 0) == 42


def test_double_grades():
    grades = [18, 28]
    assert compute_hw_average(grades, 0) == 23


def test_drop_lowest_grade_zeros():
    grades = [10,20,30]
    assert compute_hw_average(grades, 1) == 25
