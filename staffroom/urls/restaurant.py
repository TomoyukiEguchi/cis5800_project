
from django.urls import path
from staffroom.views import RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView, TimeSlotUpdateView, SocialMediaUpdateView

app_name = "restaurant"

urlpatterns = [
    path('create', RestaurantCreateView.as_view(), name="create"),
    path('<int:pk>/update', RestaurantUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', RestaurantDeleteView.as_view(), name="delete"),
    path('<int:pk>/timeslot', TimeSlotUpdateView.as_view(), name="timeslot"),
    path('<int:pk>/socialmedia', SocialMediaUpdateView.as_view(), name="social"),
]