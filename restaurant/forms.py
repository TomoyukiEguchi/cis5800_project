from django import forms

from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['name', 'area', 'cuisine', 'live_capacity', 'address1', 'address2', 'city', 'state', 'zipcode', "user", ]

        widgets = {
            "user": forms.HiddenInput()
        }


class TimeSlotForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['lunch9', 'lunch10', 'lunch11', 'lunch12', 'lunch1', 'lunch2', 'dinner5', 'dinner6', 'dinner7', 'dinner8', 'dinner9', 'dinner10', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # labels = {
        #     'dinner5': 'Dinner 5:00',
        #     'dinner6': 'Dinner 6:00',
        #     'dinner7': 'Dinner 7:00',
        #     'dinner8': 'Dinner 8:00',
        #     'dinner9': 'Dinner 9:00',
        #     'dinner10': 'Dinner 10:00',
        # }


class SearchForm(forms.Form):
    q = forms.CharField(min_length=1, max_length=20, label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

