from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.get_home_page, name='get_home_page'),
    path('summernote/', include('django_summernote.urls')),
    path('user_page/', views.user_page, name='user_page'),
    path('add_workout/', views.AddWorkoutView.as_view(), name='add_workout'),
    path('details/<slug:slug>/',views.WorkoutDetail.as_view(), name='workout_detail'),
    path('like_workout_detail/<slug:slug>/', views.like_workout_detail, name='like_workout_detail'),
    path('edit/<slug:slug>', views.WorkoutUpdateView.as_view(), name='edit_workout'),
    path('<slug:slug>/delete/', views.WorkoutDeleteView.as_view(), name='workout_delete'),
    path('delete/<int:workout_id>/',views.workout_delete_confirmation, name='workout_delete_confirmation'),
]
