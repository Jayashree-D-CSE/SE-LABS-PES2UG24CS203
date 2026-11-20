def average_marks(marks_csv):
    if not isinstance(marks_csv, str) or not marks_csv.strip():
        raise ValueError("Marks input must be a non-empty string")

    try:
        marks = [int(m.strip()) for m in marks_csv.split(',')]

        if not marks:
            raise ValueError("At least one mark is required")

        if any(mark < 0 or mark > 100 for mark in marks):
            raise ValueError("Marks must be between 0 and 100")

        return round(sum(marks) / len(marks), 2)

    except ValueError as e:
        raise ValueError(f"Invalid marks input: {e}")


def parse_srn(srn):
    if not isinstance(srn, str):
        raise ValueError("SRN must be a string")

    if len(srn) != 13:
        raise ValueError("SRN must contain exactly 13 characters")

    if not (
        srn[:3].isalpha()
        and srn[3].isdigit()
        and srn[4:6].isalpha()
        and srn[6:8].isdigit()
        and srn[8:10].isalpha()
        and srn[10:].isdigit()
    ):
        raise ValueError("Invalid SRN format")

    return srn[:4], int(srn[6:8]), srn[8:10]


def short_name(full_name):
    if not isinstance(full_name, str) or not full_name.strip():
        raise ValueError("Name must be a non-empty string")

    parts = full_name.split()

    if len(parts) < 2:
        raise ValueError("Please enter at least first and last name")

    first = parts[0]
    last = parts[-1]

    return first[0].upper() + ". " + last.capitalize()


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    print("Short Name:", result)


if __name__ == "__main__":
    main()