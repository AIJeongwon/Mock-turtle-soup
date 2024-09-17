from django.shortcuts import render
from django.http import HttpResponse
from django .views.generic import View
from .models import *

# Create your views here.
class question_view(View):
    context = {}
    template_name = "question_list.html"
    def get(self, request):
        questions_list = Question.objects.all()
        self.context = {"questions_list" : questions_list}
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        return render(request, self.template_name, self.context)

class start_chat(View):
    context = {}
    template_name = "start_chat.html"
    def get(self, request):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        return render(request, self.template_name, self.context)