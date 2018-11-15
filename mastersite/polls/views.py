from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {'latest_questions':latest_questions})
    return render_to_string(template.render({'latest_questions':latest_questions}))


def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" % question_id)


def results(request, question_id):
    return HttpResponse("These are the results of question: %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
