from django.urls import path

from . import views

app_name="myapp"
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/SpringPhoto/", views.Springs.as_view(), name="SpringPhoto"),
    path("home/SummerPhoto/", views.Summers.as_view(), name="SummerPhoto"),
    path("home/AutumnPhoto/", views.Autumns.as_view(), name="AutumnPhoto"),
    path("home/WinterPhoto/", views.Winters.as_view(), name="WinterPhoto"),
    path("home/SiteInfo/", views.SiteInfo.as_view(), name="SiteInfo"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]