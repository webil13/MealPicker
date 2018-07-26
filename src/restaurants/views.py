from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import RestaurantCreateForm
from .models import RestaurantLocation

# Create your views here.

def restaurant_createview(request):
    template_name = 'restaurants/form.html'
    context = {}
    return render(request, template_name, context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def restaurant_detailview(request, slug):
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        "object": obj
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    # template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj

# class SearchRestaurantListView(ListView):
#     template_name = 'restaurants/restaurants_list.html'

#     def get_queryset(self):
#         print(self.kwargs)
#         slug = self.kwargs.get("slug")
#         if slug:
#             queryset = RestaurantLocation.objects.filter(
#                 Q(category__iexact=slug) |
#                 Q(category__icontains=slug)
#             )
#         else:
#             queryset = RestaurantLocation.objects.none
#         return queryset


# function based view 

# def home(request):
    

#     return render(request, "home.html", context)

# def about(request):
#     context = {
#     }

#     return render(request, "about.html", context)

# def contact(request):
#     context = {
#     }

#     return render(request, "contact.html", context)

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)

# def post(self, request, *args, **kwargs):
#     context = {}
#     return render(request, "contact.html", context)

# def put(self, request, *args, **kwargs):
#     context = {}
#     return render(request, "contact.html", context)

# class based views

# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         num = None
#         some_list = [
#             random.randint(0, 100000000),
#             random.randint(0, 100000000),
#             random.randint(0, 100000000),
#         ]
#         condition_bool_item = True
#         if condition_bool_item:
#             num = random.randint(0, 100000000)
#         context = {
#             "num": num,
#             "some_list": some_list
#         }
#         return context

# class AboutView(TemplateView):
#     template_name = 'about.html'

# class ContactView(TemplateView):
#     template_name = 'contact.html'# Create your views here.

# function based view 
# def home(request):
    

#     return render(request, "home.html", context)

# def about(request):
#     context = {
#     }

#     return render(request, "about.html", context)

# def contact(request):
#     context = {
#     }

#     return render(request, "contact.html", context)

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)

# def post(self, request, *args, **kwargs):
#     context = {}
#     return render(request, "contact.html", context)

# def put(self, request, *args, **kwargs):
#     context = {}
#     return render(request, "contact.html", context)

# class based views

# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         num = None
#         some_list = [
#             random.randint(0, 100000000),
#             random.randint(0, 100000000),
#             random.randint(0, 100000000),
#         ]
#         condition_bool_item = True
#         if condition_bool_item:
#             num = random.randint(0, 100000000)
#         context = {
#             "num": num,
#             "some_list": some_list
#         }
#         return context

# class AboutView(TemplateView):
#     template_name = 'about.html'

# class ContactView(TemplateView):
#     template_name = 'contact.html'