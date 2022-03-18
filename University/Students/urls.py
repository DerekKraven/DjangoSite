from django.urls import path
from .views import *

urlpatterns = [
   path('', index, name='index'),
   path('student/add', student_add, name='student_add'),
   path('group/add', group_add, name='group_add'),
   path('authorization/', authorization, name='authorization'),
   path('registration/', registration, name='registration'),
]
