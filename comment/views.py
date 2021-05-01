from django.shortcuts import redirect
from django.contrib import messages
from comment.forms import CommentForm


def comment_create(request):
    
    full_name = request.POST.get("full_name")
    phone_number = request.POST.get("phone_number")
    email_address = request.POST.get("email")

    restaurant_id = request.POST.get("restaurant")
    content = request.POST.get("content")

    data = {"full_name": full_name, "phone_number": phone_number, "email": email_address, "content": content, "restaurant": restaurant_id}

    form = CommentForm(data=data)
    if form.is_valid():
        form.save()
        # messages.success(request, "Your comment has been sent.")
    else:
        messages.error(request, "Your comment has not been sent.")

    return redirect("restaurant:pre_order_confirm", pk=restaurant_id)
    # return redirect("restaurant:detail", pk=restaurant_id)