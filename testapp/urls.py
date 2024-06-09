from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/',views.home),
    path('newuser/', views.newuser),
    path('insertuser/', views.insertuser),
    path('viewusers/',views.viewusers, name='viewusers'),
    path('viewusers/<int:user_id>', views.get_user_details, name='user_details')
    
]
urlpatterns += staticfiles_urlpatterns()