from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from base import views

urlpatterns = [

    path('home/', views.home, name = 'home'),
    # path('product/<int:product_id>', views.product),
    path('product/<int:product_id>', views.ProductView.as_view()),
    path( 'about/' , views.AboutView.as_view()),
    path( 'report/' , views.report),


    ################### sign up

    # path( 'signup/' , views.signup),               # sign up def based
    path( 'signup/' , views.SignUpView.as_view()),   # sign up class based

    ################### login

    # path( 'login/' , views.signin, name = 'login'),
    path('login/', auth_views.LoginView.as_view(), name="login"),  # vaghti ke Login be tore auto anjam mishavad


    ################### logout
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),  # vaghti ke Login be tore auto anjam mishavad

]