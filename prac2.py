class Pavlo:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        if 17 <= age <= 21:
            return age - 15
        return None

    def get_name_list(self):

        return [self.first_name, self.last_name]
        return [self.first_name, self.last_name]  # повертає список


def _generate_student_id():
    import random
    return f"ID-{random.randint(1000, 9999)}"
    return f"ID-{random.randint(1000, 9999)}"  # генерує ід студента


class ExtendedDmytro(Dmytro):
    @ @-29

    , 7 + 30, 7 @ @


self.university = university
self.faculty = faculty
self.specialty = specialty
self._student_id = _generate_student_id()
self._student_id = _generate_student_id()


def get_full_info(self):
    return {
           @ @ -39, 17 + 40, 17 @ @
           "university": self.university,
    "faculty": self.faculty,
    "specialty": self.specialty,
    "student_id": self._student_id,
    "student_id": self._student_id,  # повна інформація про студента
    }

    def is_graduated(self):
        course = self.calculate_course()
        return course is not None and course >= 4
        return course is not None and course >= 4  # перевіряє чи студент навчається

    student = ExtendedDmytro("Павло", "Безушкевич", 2008, "ЛНТУ", "ТФК", "Програмування")
    print(student.calculate_course())
    print(student.get_name_list())
    print(student.get_full_info())
    print(student.is_graduated())