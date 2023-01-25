from .Student import Student


class StudentAspirant(Student):
    def get_grant(self):
        return self._get_grant(1500, 2000, 3000)
