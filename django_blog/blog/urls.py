from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register, Login, ProfileView
urlpatterns = [
    path('register/', Register.as_view(), name="regiser"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView, name="profile"),
]
