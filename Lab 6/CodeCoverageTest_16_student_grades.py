
import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# Tests for letter_grade()

def test_letter_grade_s():
    assert letter_grade(95) == "S"


def test_letter_grade_a():
    assert letter_grade(85) == "A"


def test_letter_grade_b():
    assert letter_grade(75) == "B"


def test_letter_grade_c():
    assert letter_grade(65) == "C"


def test_letter_grade_d():
    assert letter_grade(55) == "D"


def test_letter_grade_e():
    assert letter_grade(45) == "E"


def test_letter_grade_f():
    assert letter_grade(30) == "F"


def test_letter_grade_zero():
    assert letter_grade(0) == "F"


def test_letter_grade_hundred():
    assert letter_grade(100) == "S"


def test_letter_grade_negative_marks():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-1)


def test_letter_grade_marks_above_100():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(101)


# Tests for final_marks()

def test_final_marks_without_project():
    assert final_marks(30, 50, False) == 80


def test_final_marks_with_project():
    assert final_marks(30, 50, True) == 85


def test_final_marks_project_bonus_capped_at_100():
    assert final_marks(40, 60, True) == 100


def test_final_marks_internal_above_limit():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(41, 50, False)


def test_final_marks_external_above_limit():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(30, 61, False)


def test_final_marks_zero():
    assert final_marks(0, 0, False) == 0


# Tests for exam_eligibility()

def test_exam_eligibility_fees_not_paid():
    assert exam_eligibility(90, False, False) == "blocked"


def test_exam_eligibility_attendance_above_75():
    assert exam_eligibility(80, True, False) == "eligible"


def test_exam_eligibility_attendance_exactly_75():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_eligibility_medical_exception():
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_eligibility_below_medical_threshold():
    assert exam_eligibility(60, True, True) == "detained"


def test_exam_eligibility_low_attendance_without_medical():
    assert exam_eligibility(70, True, False) == "detained"

