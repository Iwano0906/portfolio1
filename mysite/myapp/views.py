from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


from . import forms

class TopView(TemplateView):
    template_name = "myapp/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "myapp/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "myapp/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "myapp/login.html"

#プルダウンメニュー
class Springs(LoginRequiredMixin, TemplateView):
    template_name = "myapp/SpringPhoto.html"

class Summers(LoginRequiredMixin, TemplateView):
    template_name = "myapp/SummerPhoto.html"

class Autumns(LoginRequiredMixin, TemplateView):
    template_name = "myapp/AutumnPhoto.html"

class Winters(LoginRequiredMixin, TemplateView):
    template_name = "myapp/WinterPhoto.html"

class SiteInfo(LoginRequiredMixin, TemplateView):
    template_name = "myapp/SiteInfo.html"    