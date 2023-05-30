from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from password_manager.models import ListablePassword
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class CustomLogin(LoginView):
    template_name = "password_manager/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("password_list")

class AccountCreation(FormView):
    template_name = "password_manager/account_creation.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("password_list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(AccountCreation, self).form_valid(form)
    
    def get(self, *arg, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("password_list")
        return super(AccountCreation, self).get( *arg, **kwargs)

class PasswordList(LoginRequiredMixin, ListView):
    model = ListablePassword
    template_name = "password_manager/password_list.html"
    context_object_name = "password_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["password_list"] = context["password_list"].filter(user=self.request.user)
        return context

class PasswordDetails(LoginRequiredMixin, DetailView):
    model = ListablePassword
    context_object_name = "password"
    template_name = "password_manager/password_details.html"

    #remove all other #-marks on this class
    #def get(self, *arg, **kwargs):
    #    self.object = self.get_object()
    #    context = super().get_context_data(**kwargs)
    #    if self.request.user == context["password"].user:
    #        return super(PasswordDetails, self).get( *arg, **kwargs)
    #    return redirect("password_list")
        


class PasswordCreation(LoginRequiredMixin, CreateView):
    model = ListablePassword
    template_name = "password_manager/password_creation.html"
    fields = ["password", "web_address"]
    success_url = reverse_lazy("password_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PasswordCreation, self).form_valid(form)

class PasswordUpdating(LoginRequiredMixin, UpdateView):
    model = ListablePassword
    fields = ["password", "web_address"]
    success_url = reverse_lazy("password_list")

class PasswordDeletion(LoginRequiredMixin, DeleteView):
    model = ListablePassword
    template_name = "password_manager/password_confirm_delete.html"
    context_object_name = "password"
    success_url = reverse_lazy("password_list")