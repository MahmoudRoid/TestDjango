from django.urls import path
from django.views.generic import TemplateView

from base import views

urlpatterns = [

    path('home/', views.home),
    # path('product/<int:product_id>', views.product),
    path('product/<int:product_id>', views.ProductView.as_view()),
    path( 'about/' , views.AboutView.as_view()),
    path( 'report/' , views.report),

]