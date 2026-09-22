# -----------------------------------------
# Semester Grade Program
# -----------------------------------------

def ceil(x):
    """Round a number UP to the nearest integer."""
    if int(x) == x:
        return int(x)
    else:
        return int(x) + 1


def semesterGrade(midterm, final):
    """Return the semester letter grade."""
    # Final counts twice as much as midterm
    average = (midterm + 2 * final) / 3

    # Round UP to nearest whole number
    rounded = ceil(average)

    # Assign letter grade
    if 90 <= rounded <= 100:
        return "A"
    elif 80 <= rounded <= 89:
        return "B"
    elif 70 <= rounded <= 79:
        return "C"
    elif 60 <= rounded <= 69:
        return "D"
    else:
        return "F"


def main():
    midterm = float(input("Enter midterm grade: "))
    final = float(input("Enter final exam grade: "))

    grade = semesterGrade(midterm, final)
    print(f"Semester grade: {grade}")


# Run the program
main()
