from .aspirant import create_aspirant, calculate_aspirant_grant
from .bachelor import create_bachelor, calculate_bachelor_grant
from .student import update_average_grade


def test():
    bachelor = create_bachelor('Ilnur', '2012', 4.3)
    aspirant = create_aspirant('Roman', '312', 5)
    print(bachelor, calculate_bachelor_grant(bachelor))
    print(aspirant, calculate_aspirant_grant(aspirant))
    bachelor = update_average_grade(bachelor, 3.4)
    aspirant = update_average_grade(aspirant, 4.4)
    print(bachelor, calculate_bachelor_grant(bachelor))
    print(aspirant, calculate_aspirant_grant(aspirant))


if __name__ == '__main__':
    test()
