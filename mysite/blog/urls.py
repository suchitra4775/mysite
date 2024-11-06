from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('AllPost/',views.Allpost,name='post_data'),
    path('postinfo/<slug:slug>/',views.Postinfo,name='postinfo')
]


