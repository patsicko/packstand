from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('about/', views.about, name='about' ),
    path('details/<int:id>',views.details, name='details'),
    path("blogs",views.blogs, name = "blogs"),
    path("__reload__/", include("django_browser_reload.urls")),
    path('signup',views.signup, name="signup"),
    path('login',views.login, name="login")

]