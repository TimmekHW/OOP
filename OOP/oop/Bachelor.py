from .Student import Student


class StudentBachelor(Student):
    def get_grant(self):
        return self._get_grant(3500, 4500, 5000)
