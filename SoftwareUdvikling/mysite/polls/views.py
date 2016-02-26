from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from.models import Subject
from django.template import loader

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latestSubjectList = Subject.objects.order_by('-pub_date')[:5]
    output = ' , '.join([s.subjectTitle for s in latestSubjectList])
    return HttpResponse(output)
