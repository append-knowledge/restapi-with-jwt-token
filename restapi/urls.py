from django.urls import path
from restapi import views

urlpatterns=[
    path('accounts/signup',views.UserCreationView.as_view()),
    path('accounts/signin',views.UserSignInviews.as_view()),
    path('accounts/list',views.Userlist.as_view()),
    path('accounts/<int:id>',views.SelectedUser.as_view())
]