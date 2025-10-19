from django.urls import path
from portfolio_2 import views

app_name = 'portfolio'

urlpatterns = [
    path('portfolio_home/', views.home, name='home'),
    path('p1/', views.p1, name='p1'),
    path('p2/', views.p2, name='p2'),
    path('p3/', views.p3, name='p3'),
]