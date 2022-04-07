from quopri import decodestring

from framework_patterns.prototype import PrototypeMixin


class User:
    """ Класс пользователя"""

    def __init__(self, name):
        self.name = name


class Teacher(User):
    """Модель преподавателя"""

    def __init__(self, name):
        super.__init__(name)
        self.subject = []


class Student(User):
    """Модель студента"""

    def __init__(self, name):
        super.__init__(name)
        self.courses = []


class UserFactory:
    """Фабричный паттерн"""

    types = {
        'student': Student,
        'teacher': Teacher
    }

    @staticmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class Subject:
    def __init__(self):
        self.observe = []


class Category:
    """ Модель категории. id = автоинкремент"""

    id = 0

    def __getitem__(self, item):
        return self.courses[item]

    def __init__(self, name, category):
        self.id = Category.id
        Category.id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        """Подсчет курсов"""

        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


class Course(PrototypeMixin, Subject):
    """Модель курса"""

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)
        self.students = []
        super.__init__()

    def __getitem__(self, item):
        return self.students[item]

    def add_student(self, student: Student):
        self.students.append(student)
        student.courses.append(self)


class InteractiveCourse(Course):
    """Модель интерактивных курсов."""

    pass


class RecordCourse(Course):
    """Модель курсов в записи."""

    pass


class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        'record': RecordCourse
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class TrainingSite:
    """ Основная модель """

    def __init__(self):
        self.students = []
        self.teacher = []
        self.courses = []
        self.categories = []

    def create_user(self, type_, name):
        """
        Создаем пользователя в зависимости
         от типа (преподаватель / студент)
         """

        return UserFactory.create(type_, name)

    def create_category(self, name, category=None):
        return Category(name, category)

    def create_course(self, type_, name, category):
        return CourseFactory.create(type_, name, category)

    def find_category(self, id):
        for item in self.categories:
            print(f'{item.id}')
            item.id = id
            return item
        raise Exception(f'Category - {id} not found')

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item

    def get_student(self, name):
        for item in self.students:
            if item.name == name:
                return item

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = decodestring(val_b)
        return val_decode_str.decode('UTF-8')






