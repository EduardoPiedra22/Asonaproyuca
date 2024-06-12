from django.urls import path
from .views import *


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/password/', ResetPassWordView.as_view(), name='reset_password'),
    path('change/password/<str:token>/',
         ChangePassWordView.as_view(), name='change_password'),

]
