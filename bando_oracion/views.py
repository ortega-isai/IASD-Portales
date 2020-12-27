from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView, View
from django.contrib.messages.views import SuccessMessageMixin
from .models import Oracion
from . import forms


class OracionListView(ListView):
    model = Oracion


class TimeLineListView(ListView):
    model = Oracion
    template_name = 'bando_oracion/oracion_timeline.html'

    def get_queryset(self):
        return Oracion.objects.filter(fecha_hora__gte=timezone.now())[:12]


class OracionDetailView(DetailView):
    model = Oracion


class OracionCreate(SuccessMessageMixin, CreateView):
    model = Oracion
    form_class = forms.OracionAddForm
    success_message = "Fue creado exitosamente"


class OracionUpdate(SuccessMessageMixin, UpdateView):
    model = Oracion
    form_class = forms.OracionUpdateForm
    success_message = "Fue actualizado exitosamente"
