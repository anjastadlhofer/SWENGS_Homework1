from hw1.yamod import views
from django.urls import path


urlpatterns = [
    path('countries/', views.country_list),
    path('countries/<int:pk>/', views.country_detail),
    path('songs/', views.song_list),
    path('songs/<int:pk>/', views.song_detail),
    path('person/', views.person_list),
    path('person/<int:pk>/', views.person_detail)
]