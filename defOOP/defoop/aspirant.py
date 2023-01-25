from .student import create_student, _calculate_grant


def create_aspirant(name, group, average_grade):
    return create_student(name, group, average_grade) | {
        'degree': 'aspirant'
    }

def calculate_aspirant_grant(aspirant):
    if aspirant.get('degree') != 'aspirant':
        raise ValueError
    return _calculate_grant(aspirant['average_grade'], 3500, 4500, 5000)
