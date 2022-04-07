from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext, context
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import Task, UserInfo, Users, UserProfileManager
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    logout(request)
    username = password = ''
    try:
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('tasks'))
    except Exception as e:
        print(e)
    return render(request, 'base/login.html')


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(forms.ModelForm):
    username = forms.CharField()
    organizationName = forms.CharField()
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    zipCode = forms.IntegerField()

    class Meta:
        model = UserInfo
        fields = ("username",)


def set_password(self, raw_password):
    self.password = make_password(raw_password)


def user(request):
    if request.method == 'POST':
        username = request.POST['username']
        organizationName = request.POST['organizationName']
        password = request.POST['password']
        zipCode = request.POST['zipCode']
        email = request.POST['email']
        is_active = True
        is_staff = True
        password1 = make_password(password)

        user = Users.object.create(username=username, organizationName=organizationName, password=password1,
                                   zipCode=zipCode, email=email, is_active=is_active, is_staff=is_staff)

    return redirect("http://127.0.0.1:8000/login/?next=/")


class RegisterPageFormView(FormView):
    template_name = 'base/register.html'
    form_class = RegisterPage
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    # def form_valid(self, form):
    #     user = form.UserInfo()
    #     if user is not None:
    #         login(self.request, user)
    #     return super(RegisterPageFormView, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter()
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
    fields = ['food_name', 'description', 'quantity', 'created']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = fields = ['food_name', 'description', 'quantity', 'created']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
