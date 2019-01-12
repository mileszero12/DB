from django.shortcuts import render

# Create your views here.
from .models import Food, FoodType

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_food = Food.objects.all().count()
    #num_foodType = FoodType.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_food':num_food},#,'num_foodType':num_foodType},
    )

from django.views import generic

class FoodListView(generic.ListView):
    model = Food

class FoodTypeListView(generic.ListView):
    model = FoodType

class FoodDetailView(generic.DetailView):
    model = Food

