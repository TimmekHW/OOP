from .student import create_student, _calculate_grant


def create_bachelor(name, group, average_grade):
    return create_student(name, group, average_grade) | {
        'degree': 'bachelor'
    }

def calculate_bachelor_grant(bachelor):
    if bachelor.get('degree') != 'bachelor':
        raise ValueError
    return _calculate_grant(bachelor['average_grade'], 1500, 2000, 3000)