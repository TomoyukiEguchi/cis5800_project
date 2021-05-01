from django.views.generic import TemplateView

from restaurant.models import Restaurant


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant_list = Restaurant.objects.all().order_by('-created_at')[:8]
        
        try:
            restaurant_top = Restaurant.objects.order_by('?')[0]
        except IndexError:
            restaurant_top = None

        context = {
            'restaurant_list': restaurant_list,
            'restaurant_top': restaurant_top,
        }
        return context


class Contact(TemplateView):
    template_name = "contact.html"


class AboutUs(TemplateView):
    template_name = "about.html"