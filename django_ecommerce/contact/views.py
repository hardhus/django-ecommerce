from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactView

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactView(request.POST)
        if form.is_valid():
            out_form = form.save(commit=False)
            out_form.save()
            messages.add_message(
                request,
                messages.INFO,
                "Your message has been sent. Thank you."
            )
            return redirect("/")
    else:
        form = ContactView()
    return render(
        request,
        "contact.html",
        {"form": form,},
    )