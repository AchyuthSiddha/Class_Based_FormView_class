from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse

class CBV_Form(FormView):
    template_name='CBV_Form.html'
    form_class=SchoolForm


    def form_valid(self, form):
        form.save()
        return HttpResponse("data inserted sucessfully:")