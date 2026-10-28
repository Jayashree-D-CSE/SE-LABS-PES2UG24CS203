
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# Branch tests for letter_grade()

def test_grade_negative_marks_branch():
    with pytest.raises(ValueError):
        letter_grade(-1)


def test_grade_above_100_branch():
    with pytest.raises(ValueError):
        letter_grade(101)


def test_grade_exactly_90():
    assert letter_grade(90) == "S"


def test_grade_exactly_80():
    assert letter_grade(80) == "A"


def test_grade_exactly_70():
    assert letter_grade(70) == "B"


def test_grade_exactly_60():
    assert letter_grade(60) == "C"


def test_grade_exactly_50():
    assert letter_grade(50) == "D"


def test_grade_exactly_40():
    assert letter_grade(40) == "E"


def test_grade_below_40():
    assert letter_grade(39) == "F"


# Branch tests for final_marks()

def test_internal_marks_above_limit():
    with pytest.raises(ValueError):
        final_marks(41, 50, False)


def test_external_marks_above_limit():
    with pytest.raises(ValueError):
        final_marks(30, 61, False)


def test_internal_and_external_within_limits():
    assert final_marks(40, 60, False) == 100


def test_project_bonus_does_not_exceed_100():
    assert final_marks(30, 50, True) == 85


def test_project_bonus_exceeds_100_and_is_capped():
    assert final_marks(40, 60, True) == 100


def test_no_project_bonus():
    assert final_marks(20, 30, False) == 50


# Branch tests for exam_eligibility()

def test_fees_unpaid_branch():
    assert exam_eligibility(90, False, False) == "blocked"


def test_fees_paid_and_attendance_75():
    assert exam_eligibility(75, True, False) == "eligible"


def test_fees_paid_and_attendance_below_75():
    assert exam_eligibility(70, True, False) == "detained"


def test_medical_exception_with_attendance_65():
    assert exam_eligibility(65, True, True) == "eligible"


def test_medical_exception_below_65():
    assert exam_eligibility(64, True, True) == "detained"


def test_attendance_below_65_without_medical_exception():
    assert exam_eligibility(60, True, False) == "detained"


def test_medical_exception_not_needed_above_75():
    assert exam_eligibility(80, True, False) == "eligible"

