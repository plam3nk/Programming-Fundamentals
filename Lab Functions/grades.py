def type_of_grade(grade):
    if 2 <= grade < 3:
        return "Fail"
    elif 3.00 <= grade < 3.5:
        return "Poor"
    elif 3.50 <= grade < 4.5:
        return "Good"
    elif 4.50 <= grade < 5.5:
        return "Very Good"
    elif 5.50 <= grade <= 6:
        return "Excellent"


input_grade = float(input())
print(type_of_grade(input_grade))

