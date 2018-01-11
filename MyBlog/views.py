from django.http import HttpResponse
from django.template import loader

from .models import ForumQuestions


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def index(request):
    template=loader.get_template('MyBlog/index.html')
    return HttpResponse(template.render(),request)


def querytion_list(request):
    question_list = ForumQuestions.objects
    template = loader.get_template('MyBlog/list.html')
    context = {
        'question_list': question_list
    }
    return HttpResponse(template.render(context), request)
