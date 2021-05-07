from django.urls import path
from .views import RegisterView

app_name = 'users'

urlpatterns = [
    path('users-register/', RegisterView.as_view(), name="users register"),
]
