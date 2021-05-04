from django import forms

from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['name', 'area', 'cuisine', 'address1', 'address2', 'city', 'state', 'zipcode', "image", "user", ]

        widgets = {
            "user": forms.HiddenInput()
        }


class TimeSlotForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['live_capacity', 'lunch9', 'lunch10', 'lunch11', 'lunch12', 'lunch1', 'lunch2', 'dinner5', 'dinner6', 'dinner7', 'dinner8', 'dinner9', 'dinner10', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SocialMediaForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['facebook', 'instagram', 'twitter', ]


class SearchForm(forms.Form):
    q = forms.CharField(min_length=1, max_length=20, label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

