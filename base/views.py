from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import login

from .models import Task, Users


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(forms.Form):
    username = forms.CharField()
    organizationName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    zipCode = forms.IntegerField()

    class Meta:
        model=Users


    # def save(self, commit=True):
    #     user=super(RegisterPage, self).save(commit=False)
    #
    #     if commit:
    #         user.save()
    #     return user
        #user.set_password(self.cleaned_data[])

class RegisterPageFormView(FormView):
    template_name = 'base/register.html'
    form_class = RegisterPage
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form): 
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageFormView, self).form_valid(form)

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('tasks')
    #     return super(RegisterPage, self).get(*args, **kwargs)





class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user= self.request.user)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)
        
        context['search_input'] = search_input
        return context

        




class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task 
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'quantity', 'created']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = fields = ['title', 'description', 'quantity', 'created']
    success_url = reverse_lazy('tasks') 



class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task 
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')  
    



    

