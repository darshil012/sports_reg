from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Activity, Applicant
from .forms import ApplicantForm

from datetime import date

# Create your views here.

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -\
         ((today.month, today.day) <
         (birthDate.month, birthDate.day))
 
    return age

class MainFormView(CreateView, SuccessMessageMixin):
    template_name = 'index.html'
    form_class = ApplicantForm
    model = Applicant

    def get_success_url(self):
        return reverse_lazy('confirm', kwargs={'pk': self.object.pk})  

class ConfirmView(DetailView):
    template_name = 'confirm.html'
    model = Applicant
    context_object_name = 'applicant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applicant = Applicant.objects.get(pk=self.kwargs['pk'])
        context['age'] = calculateAge(applicant.birth_date)
        context['amount'] = applicant.activity.amount
        return context

def get_amount(request):
    activity_id = request.GET.get('activity_pk')
    amount = Activity.objects.get(id=activity_id).amount
    return HttpResponse(amount)
