from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import question
from django.template import loader
from django.db.models import F
from django.urls import reverse
from .models import Choices, question


# Create your views here.
def index(request):
    latest_question_list = question.objects.order_by("-pub_date")
    context = {'latest_question_list':latest_question_list}
    return render(request, "polls/index.html", context )

def Detail(request, question_id):
   
    qn = get_object_or_404(question, pk = question_id)
    
    return render(request, 'polls/detail.html', {"question":qn})

def Result(request, question_id):
    qn = get_object_or_404(question, pk = question_id)
    return render(request, "polls/result.html", {'question':qn})

def Vote(request, question_id):
    qn = get_object_or_404(question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choices.DoesNotExist):
        #re display the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": qn,
                "error_message": "you didin't select a choice.",
            },
        )
    else:
        selected_choice.votes = F('vote') + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args =(question.id)))