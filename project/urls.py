from django.urls import path
from project import views

urlpatterns=[
    path('accounts/signup',views.SignUpview.as_view(),name='signup'),
    path('accounts/signin',views.SignInView.as_view(),name='signin'),
    path('accounts/signout',views.SignOutView.as_view(),name='logout'),
    path('accounts/home',views.HomeView.as_view(),name='home'),
    path('accounts/change/<int:id>',views.ChangeDetailsView.as_view(),name='editdetails'),
    path('accounts/remove/<int:id>',views.delete,name='removeitem')

]