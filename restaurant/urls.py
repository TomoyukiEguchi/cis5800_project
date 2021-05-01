from django.urls import path

from restaurant.views import RestaurantListView,  RestaurantDetailView, ConfirmPreOrder, SearchListView, CuisineListView


app_name = 'restaurant'

urlpatterns = [
    path('', RestaurantListView.as_view(), name="index"),
    path('<int:pk>', RestaurantDetailView.as_view(), name="detail"),
    path('<int:pk>/confirmation', ConfirmPreOrder.as_view(), name="pre_order_confirm"),
    path('search', SearchListView, name="search"),
    path('cuisine', CuisineListView.as_view(), name="cuisine"),
]