class CourseGroup(list):
    def __init__(self, teacher: str):
        super().__init__()
        self.teacher = teacher

    def add_student(self, student: str):
        self.append(student)

    def rem_student(self, student: str):
        self.remove(student)

    def __str__(self):
        return f'{self.teacher}: ' + super().__str__()


P223 = CourseGroup('Gennadiy')
P223.extend((
    'Alexey',
    'Tatjana',
    'Aynur',
    'Svyatoslav',
    'Alla',
    'Anatoliy',
    'Ivan'
))
P223.add_student('Maria')
print(P223)
