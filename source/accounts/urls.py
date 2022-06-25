from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import UserProfileView, RegisterView, UserUpdateView

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/', UserProfileView.as_view(), name="user_profile"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegisterView.as_view(), name="registration"),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
]