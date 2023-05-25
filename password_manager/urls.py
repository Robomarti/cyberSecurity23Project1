from django.urls import path
from .views import PasswordList, PasswordDetails, PasswordCreation, PasswordUpdating, PasswordDeletion, CustomLogin, AccountCreation
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('account_creation/', AccountCreation.as_view(), name='account_creation'),
    path('', PasswordList.as_view(), name='password_list'),
    path('password/<int:pk>/', PasswordDetails.as_view(), name='password'),
    path('password-creation/', PasswordCreation.as_view(), name='password-creation'),
    path('password-updating/<int:pk>/', PasswordUpdating.as_view(), name='password-updating'),
    path('password-deletion/<int:pk>/', PasswordDeletion.as_view(), name='password-deletion'),
]
