from django.urls import path
from .views import RegisterView, CustomLoginView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('profile/me/', UserProfileView.as_view(), name="profile"),
]
