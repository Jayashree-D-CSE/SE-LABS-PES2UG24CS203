from hypothesis import given, strategies as st
from student_grades import average_marks, parse_srn, short_name


# Test 1: Fuzz testing average_marks
@given(st.one_of(st.text(), st.none()))
def test_average_marks_no_crash(s):
    try:
        average_marks(s)
    except ValueError:
        pass


# Test 2: Fuzz testing parse_srn
@given(st.one_of(st.text(), st.none()))
def test_parse_srn_no_crash(s):
    try:
        parse_srn(s)
    except ValueError:
        pass


# Test 3: Fuzz testing short_name
@given(st.one_of(st.text(), st.none()))
def test_short_name_no_crash(s):
    try:
        short_name(s)
    except ValueError:
        pass


# Test valid average marks
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_average_marks_valid(marks):
    csv = ",".join(map(str, marks))
    expected = round(sum(marks) / len(marks), 2)
    assert average_marks(csv) == expected


# Test valid SRN
@given(st.integers(min_value=0, max_value=99))
def test_parse_srn_valid(year):
    srn = f"PES2UG{year:02d}CS203"
    assert parse_srn(srn) == ("PES2", year, "CS")


# Test valid names
@given(st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1),
       st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1))
def test_short_name_valid(first, last):
    full_name = first + " " + last
    expected = first[0].upper() + ". " + last.capitalize()
    assert short_name(full_name) == expected