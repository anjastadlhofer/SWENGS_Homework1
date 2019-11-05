from hw1.yamod import views
from django.urls import path


urlpatterns = [
    path('countries/', views.country_list),
    path('countries/<int:pk>/', views.country_detail)
]