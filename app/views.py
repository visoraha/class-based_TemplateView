 from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse

# Create your views here.

class context(TemplateView):
    template_name='context.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='vinay'
        context['age']=23
        context['mbn']=9133119384
        return context


class cbv_form(TemplateView):
    template_name='cbv_form.html'
    def get_context_data(self, **kwargs):
        ob=super().get_context_data(**kwargs)
        ob['fo']=student_form()
        return ob

    def post(self,request):
        form=student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is inserted')
