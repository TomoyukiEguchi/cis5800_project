from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy

from django.contrib import messages

from .models import Restaurant
from comment.forms import CommentForm

from .forms import SearchForm
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
class RestaurantListView(ListView):
    model = Restaurant
    paginate_by = 5

    def get_queryset(self):
        return Restaurant.objects.all().order_by('-updated_at')


class RestaurantDetailView(DetailView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['CommentForm'] = CommentForm(initial={'restaurant': self.object})

        return context


class ConfirmPreOrder(DetailView):
    template_name = 'restaurant/restaurant_confirm_pre_order.html'
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['CommentForm'] = CommentForm(initial={'restaurant': self.object})        
        
        return context


def SearchListView(request):
    if request.method == 'POST':
        searchform = SearchForm(request.POST)

        if searchform.is_valid():
            freeword = searchform.cleaned_data['q']
            search_list = Restaurant.objects.filter(Q(name__icontains = freeword)|Q(cuisine__icontains = freeword))

        params = {
            'search_list': search_list,
        }

        return render (request, 'restaurant/search.html', params)


class CuisineListView(ListView):
    template_name = 'restaurant/restaurant_cuisine_list.html'
    model = Restaurant