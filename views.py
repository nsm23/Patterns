from my_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 Ok', render('index.html', now_date=request.get('now_date'))


class DescCourse:
    def __call__(self, request):
        return '200 Ok', render('description.html', now_date=request.get('now_date'))


class Contacts:
    def __call__(self, request):
        return '200 Ok', render('contacts.html', now_date=request.get('now_date', None))


class PageNotFound:
    def __call__(self, request):
        return '404 bad', render('page_not_found.html', now_date=request.get('now_date', None))





