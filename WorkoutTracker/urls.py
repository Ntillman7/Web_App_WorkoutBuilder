from django.urls import path
from . import views


urlpatterns = [
    path('', views.workout_home, name='WT_home'),
    path('create', views.workout_create, name='WT_create'),
    path('log', views.workout_log, name='WT_log'),
    path('<int:pk>/details/', views.workout_details, name='WT_details'),
    path('<int:pk>/update/', views.workout_update, name='WT_update'),
    path('<int:pk>/delete/', views.workout_delete, name='WT_delete'),
    path('api/', views.workout_api, name='WT_api'),
    path('bsoup/', views.workout_bsoup, name='WT_bsoup'),
    path('bsoup2/', views.workout_bsoup2, name='WT_bsoup2'),
    path('lower/', views.workout_lower, name='WT_lower'),
    path('upper/', views.workout_upper, name='WT_upper'),
    path('bsoup2/save-workout/', views.workout_save, name='WT_save'),
    path('<int:pk>/fave-workout/', views.fave_workout, name='WT_faves'),
    path('fave-workouts/', views.favorite_workouts, name='WT_faves'),
    path('save-workout/', views.workout_saved_db, name='WT_save2')
]
