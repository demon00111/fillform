


from django.urls import path
from . import views
urlpatterns = [
    path('', views.formss,name="home"),
    path('submit', views.sub,name="submit"),
    path('delete/<int:pk>/', views.delete_data, name="d"),
    path('<int:id>/', views.edit_data, name="update")
    
]