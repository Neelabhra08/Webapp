from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('Homework/', views.work, name='Homework'),
    path('previous_class_report/', views.report, name='previous Class report'),
    path('profile/', views.profile, name='My Profile'),
    path('my_routine/', views.routine, name='My Routine'),

]
