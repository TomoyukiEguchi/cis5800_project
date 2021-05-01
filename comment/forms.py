from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        
        fields = ["full_name", "phone_number", "email", "content", "restaurant", ]
    
        widgets = {
                "restaurant": forms.HiddenInput()
        }