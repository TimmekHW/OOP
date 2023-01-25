from .Bachelor import StudentBachelor
from .Aspirant import StudentAspirant


def test():
    bachelor, aspirant = StudentBachelor('Petya', '142', 3.4), StudentAspirant('Semyon', 312, 4)
    print(bachelor.name, bachelor.get_grant())
    print(aspirant.name, aspirant.get_grant())
    bachelor.update_average_grade(2.3)
    aspirant.update_average_grade(5)
    print(bachelor.name, bachelor.get_grant())
    print(aspirant.name, aspirant.get_grant())


if __name__ == '__main__':
    test()
