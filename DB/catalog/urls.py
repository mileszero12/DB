from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('food/', views.FoodListView.as_view(), name='food'),
	path('foodType/', views.FoodTypeListView.as_view(), name='foodType'),
]
