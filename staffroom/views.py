from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, SignUpForm

from restaurant.models import Restaurant
from restaurant.forms import RestaurantForm, TimeSlotForm, SocialMediaForm


class StaffroomTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "staffroom/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['restaurant_list'] = Restaurant.objects.filter(user=self.request.user).prefetch_related("comment_set")
        else:
            context['restaurant_list'] = None

        return context


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm 
    success_url = reverse_lazy("staffroom:index")


    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.POST.dict()
        data['user'] = user.id
        form = RestaurantForm(data=data, files=request.FILES)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        messages.success(self.request, "Your registration completed successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Your registration cannot be completed.")
        return super().form_invalid(form)


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = ["name", "area", "cuisine", "live_capacity", "address1", "address2", "city", "state", "zipcode", ]
    success_url = reverse_lazy("staffroom:index")
    # def get_success_url(self):
    #     pk = self.kwargs.get("pk")
    #     return reverse("restaurant:detail", kwargs={"pk": pk})

    def form_valid(self, form):
        messages.success(self.request, "Your information has been successfully updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Your information has not been updated.")
        return super().form_invalid(form)


class TimeSlotUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = TimeSlotForm 
    template_name = 'restaurant/timeslot_form.html'
    success_url = reverse_lazy("staffroom:index")

    def form_valid(self, form):
        messages.success(self.request, "Your information has been successfully updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Your information has not been updated.")
        return super().form_invalid(form)


# class TimeSlotDinnerUpdateView(LoginRequiredMixin, UpdateView):
#     model = Restaurant
#     form_class = TimeSlotForm 
#     template_name = 'restaurant/timeslot_dinner_form.html'
#     success_url = reverse_lazy("staffroom:index")

#     def form_valid(self, form):
#         messages.success(self.request, "Your time slot settings completed successfully.")
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         messages.error(self.request, "Your settings for time slots cannot be completed.")
#         return super().form_invalid(form)

class SocialMediaUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = SocialMediaForm 
    template_name = 'restaurant/socialmedia_form.html'
    success_url = reverse_lazy("staffroom:index")

    def form_valid(self, form):
        messages.success(self.request, "Your information has been successfully updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Your information has not been updated.")
        return super().form_invalid(form)


class RestaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy("staffroom:index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your information has been deleted.")
        return super().delete(request, *args, **kwargs)


class Login(LoginView):
    form_class = LoginForm
    template_name = 'staffroom/login.html'

class Logout(LogoutView):
    template_name = 'staffroom/logout.html'


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'staffroom/signup.html'
    success_url = reverse_lazy('staffroom:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        messages.info(self.request, 'Your account has been successfully created.')
        return HttpResponseRedirect(self.get_success_url())
