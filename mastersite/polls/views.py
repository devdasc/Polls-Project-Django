from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.template import loader, RequestContext


# Create your views here.


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context ={ 'latest_questions': latest_questions}
    # return HttpResponse(template.render(context))
    context = {'latest_questions':latest_questions}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    #return HttpResponse("This is the detail view of the question: %s" % question_id)
    #question = Question.objects.get(pk = question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question': question})

def results(request, question_id):
    #return HttpResponse("These are the results of question: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question': question})

def vote(request, question_id):
    #return HttpResponse("Vote on question: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request,'polls/detail.html', {'question': question, 'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id)))

