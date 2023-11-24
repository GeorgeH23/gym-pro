from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.get_home_page, name='get_home_page'),
    path('summernote/', include('django_summernote.urls')),
    path('user_page/', views.user_page, name='user_page'),
    path('add_workout/', views.AddWorkoutView.as_view(), name='add_workout'),
]
