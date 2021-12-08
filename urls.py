from datetime import date
from views import *


def first_front(request):
    request['now_date'] = date.today()


def second_front(request):
    request['key'] = 'key'


fronts = [first_front, second_front]

routes = {
    '/': Index(),
    '/description/': DescCourse(),
    '/contacts/': Contacts(),
}
