from django.urls import path
from . import views


urlpatterns = [
    # path('api', views.index)
    path('api/', views.add_person),
    path('api/<str:pk>', views.update_delete_person),
] 