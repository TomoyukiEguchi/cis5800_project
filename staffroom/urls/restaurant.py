
from django.urls import path
from staffroom.views import RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView, TimeSlotLunchUpdateView, TimeSlotDinnerUpdateView

app_name = "restaurant"

urlpatterns = [
    path('create', RestaurantCreateView.as_view(), name="create"),
    path('<int:pk>/update', RestaurantUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', RestaurantDeleteView.as_view(), name="delete"),
    path('<int:pk>/timeslot_lunch', TimeSlotLunchUpdateView.as_view(), name="timeslot_lunch"),
    path('<int:pk>/timeslot_dinner', TimeSlotDinnerUpdateView.as_view(), name="timeslot_dinner"),
]