from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        
        fields = ["full_name", "phone_number", "email", "guest", "content", "restaurant", ]
    
        widgets = {
                "restaurant": forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'