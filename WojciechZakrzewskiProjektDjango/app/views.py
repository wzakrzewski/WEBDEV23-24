from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import ToDoItem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class Login(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todolist')

class Register(FormView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    redirect_anthenticated_user = True
    success_url = reverse_lazy('todolist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todolist')
        return super(Register, self).get(*args, **kwargs)    

class TodoList(LoginRequiredMixin, ListView):
    model = ToDoItem
    context_object_name = 'todolist'

    def get_queryset(self):
        user = self.request.user
        queryset = ToDoItem.objects.filter(user=user)
        return queryset

class CreateItem(LoginRequiredMixin, CreateView):
    model = ToDoItem
    fields = ['name', 'info', 'is_completed']
    success_url = reverse_lazy('todolist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateItem, self).form_valid(form)

class UpdateItem(LoginRequiredMixin, UpdateView):
    model = ToDoItem
    fields = ['name', 'info', 'is_completed']
    success_url = reverse_lazy('todolist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateItem, self).form_valid(form)

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('todolist')
