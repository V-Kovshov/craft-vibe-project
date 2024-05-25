from django.urls import path

from users.views.user_views import RegistrationView

urlpatterns = [
    path('users/reg/', RegistrationView.as_view(), name='reg')
]

