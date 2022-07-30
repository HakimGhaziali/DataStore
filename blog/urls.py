from django.urls import path
from .views import ListView , DetailView



urlpatterns = [
   
    path('', ListView.as_view() , name='list_view'),
    path('blogdetail/' , DetailView.as_view(), name='detail_view')

]
