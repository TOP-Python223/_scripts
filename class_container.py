from typing import Optional


class CourseGroup:
    def __init__(self, id_: str, course_name: str):
        self.id = id_
        self.course = course_name
        self.teacher: Optional[str] = None
        self.students: list[str] = []

    def add_student(self, student_name: str):
        self.students += [student_name]

    def remove_student(self, student_name: str):
        self.students.remove(student_name)

    def change_teacher(self, teacher_name: str):
        self.teacher = teacher_name

    def __contains__(self, person_name: str):
        return person_name in self.students or person_name == self.teacher

    def __getitem__(self, index: int):
        if isinstance(index, int):
            if index == 0:
                return self.teacher
            elif 0 < index:
                if index < len(self.students) + 1:
                    return self.students[index-1]
                else:
                    raise IndexError
            else:
                return self.students[index]
        else:
            raise TypeError

    def __setitem__(self, index: int, teacher_name: str):
        if isinstance(index, int):
            if index == 0:
                self.change_teacher(teacher_name)
            else:
                raise NotImplementedError
        else:
            raise TypeError

    def __delitem__(self, index: int):
        if isinstance(index, int):
            if index == 0:
                self.teacher = None
            else:
                raise NotImplementedError
        else:
            raise TypeError

    def __len__(self):
        return len(self.students) + (1 if self.teacher is not None else 0)

    def __str__(self):
        return f'[{self.teacher!r}, ' + str(self.students)[1:]


p223 = CourseGroup('Python223', 'Python')
p223.add_student('Алексей')
p223.add_student('Татьяна')
p223.add_student('Айнур')
p223.add_student('Святослав')
p223.add_student('Алла')
p223.add_student('Мария')
p223.add_student('Анатолий')
p223.add_student('Иван')
p223.change_teacher('Геннадий')

print('Мария' in p223)

print(f'\n{p223[0] = }')
print(f'{p223[1] = }')
print(f'{p223[-1] = }\n')
print(f'{len(p223) = }\n')

print(p223, end='\n\n')

for pers in p223:
    print(pers)
print()

p223[0] = 'Андрей'
print("p223[0] = 'Андрей'")
print(p223, end='\n\n')

# p223[1] = 'Григорий'
# print("p223[1] = 'Григорий'")
# print(p223, end='\n\n')

del p223[0]
print("del p223[0]")
print(p223, end='\n\n')
