from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from planner.models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def home(request):
    return render(request, 'base.html')


class ResourceCreateView(LoginRequiredMixin, CreateView):
    # {'title': 'Shopping List'}
    model = ResourceList
    template_name = 'components/resources.html'
    form_class = ResourceForm
    success_url = reverse_lazy("list-creation")

    def get_context_data(self, **kwargs):
        context = super(ResourceCreateView, self).get_context_data(**kwargs)
        context['ShoppingList'] = ResourceList.objects.filter(author=self.request.user)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(CreateView, self).form_valid(form)


class GuestListView(CreateView):
    model = EmailList
    template_name = 'components/guests.html'
    form_class = EmailForm
    success_url = reverse_lazy("guests")

    def get_context_data(self, **kwargs):
        context = super(GuestListView, self).get_context_data(**kwargs)
        context['GuestList'] = EmailList.objects.all()
        return context


def location_picker(request):
    return render(request, 'components/location.html', {'title': 'Locations'})


class ThemePickerView(ListView):
    model = ThemeList
    template_name = 'components/theme.html'
    success_url = reverse_lazy("theme")

    def get_context_data(self, **kwargs):
        context = super(ThemePickerView, self).get_context_data(**kwargs)
        context['Themes'] = ThemeList.objects.all()
        return context
