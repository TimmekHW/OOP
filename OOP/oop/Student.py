class Student:
    def __init__(self, name, group, average_grage):
        if not self._validate(name, group, average_grage):
            raise ValueError
        
        self.name = name
        self.group = group
        self.average_grade = average_grage

    def _validate(self, name, group, average_grade):
        return isinstance(name, str) and isinstance(group, (int, str)) and isinstance(average_grade, (int, float)) and 0 <= average_grade <= 5

    def _get_grant(self, minmum, usual, maximum):
        if self.average_grade == 5:
            return maximum
        elif 4 <= self.average_grade < 5:
            return usual
        elif 3 <= self.average_grade < 4:
            return minmum
        else:
            return 0

    def update_average_grade(self, value):
        if 0 <= value <= 5:
            self.average_grade = value 
        else:
            raise ValueError
