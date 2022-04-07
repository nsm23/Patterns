from decorators import FrameworkLog
from framework_patterns.patterns_list import TrainingSite
from my_framework.templator import render


site = TrainingSite()
logger = FrameworkLog('main')

class Index:
    def __call__(self, request):
        return "200 Ok", render("index.html", now_date=request.get("now_date"))


class DescCourse:
    def __call__(self, request):
        return "200 Ok", render("description.html", now_date=request.get("now_date"))


class Contacts:
    def __call__(self, request):
        return "200 Ok", render("contacts.html", now_date=request.get("now_date", None))


class SendMessage:
    def __call__(self, request):
        return "200 Ok", render("message.html", encode='utf-8')


class PageNotFound:
    def __call__(self, request):
        return "404 bad", render(
            "page_not_found.html", now_date=request.get("now_date", None)
        )


class Creator:
    def __call__(self, request):
        return "200 ok", render(
            "creator.html", now_date=request.get("now_date", None)
        )


class CreateCourse:
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            if category_id:
                category = site.find_category(int(category_id))
                course = site.create_course('record', name, category)
                site.courses.append(course)
            categories = site.categories
            return '200 OK', render('create_course.html', categories=categories)
        else:
            categories = site.categories
            return '200 OK', render('create_course.html', categories=categories)


class CategoryCreate:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category(int(category_id))

            new_category = site.create_category(name, category)
            site.categories.append(new_category)
            return '200 OK', render('create_category.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html', categories=categories)


class CategoryList:
    def __call__(self, request):

        return '200 OK', render('category_lists.html', objects_list=site.categories)


class StudentList:
    def __call__(self, request):
        logger.logging('Students list')
        return '200 OK', render('student_list.html', objects_list=site.students)


class StudentCreate:
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            new_obj = site.create_user('student', name)
            site.students.append(new_obj)
            return '200 OK', render('create_student.html', objects_list=site.students)
        else:
            student = site.students
            return '200 OK', render('create_student.html', categories=student)


class CopyCourse:
    def __call__(self, request):
        request_params = request['request_params']
        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)
            return '200 OK', render('lists.html', objects_list=site.courses)
        except KeyError:
            logger.logging('No course added')
            return '200 OK', 'No courses have been added yet'
