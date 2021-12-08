from wsgiref.simple_server import make_server
from my_framework.main import Framework
from urls import *


application = Framework(routes, fronts)

with make_server('', 8000, application) as page_lst:
    page_lst.serve_forever()




