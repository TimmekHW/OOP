def create_student(name, group, average_grade=0):
    if not _validate_data(name, group, average_grade):
        raise ValueError
    return {
        'class': 'student',
        'name': name,
        'group': group,
        'average_grade': average_grade
    }

def _validate_data(name, group, average_grade):
    return isinstance(name, (str)) and isinstance(group, (int, str)) and isinstance(average_grade, (int, float)) and 0 <= average_grade <= 5


def _calculate_grant(grade, minimal, usual, maximal):
    if grade == 5:
        return maximal
    elif 4 <= grade < 5:
        return usual
    elif 3 <= grade < 4:
        return minimal
    else:
        return 0


def update_average_grade(student, new_average_grade):
    student['average_grade'] = new_average_grade
    return student
