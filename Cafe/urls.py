from django.urls import path
#from Cafe.views import main_keyword_list
from . import views

app_name = "Cafe"

urlpatterns = [
    path('', views.main_page , name='main'),
    path('keyword_list/', views.main_keyword_list, name='keyword_list'),
    path('find_cafe/',views.find_cafe,name="find_cafe"),
    # path('cafe_detail/<int:pk>/',views.cafe_detail,name="cafe_detail"),
  
]