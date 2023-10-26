from django.shortcuts import render, redirect
from users.forms import SigninForm, UserForm
from users.models import User
from django.template import RequestContext
from django.db import IntegrityError
import django_ecommerce.settings as settings
import datetime


# Create your views here.
def sign_in(request):
    user = None
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            results = User.objects.filter(email=form.cleaned_data["email"])
            if len(results) == 1:
                if results[0].check_password(form.cleaned_data["password"]):
                    request.session["user"] = results[0].pk
                    return redirect("/")
                else:
                    form.addError("Incorrect email address or password")
            else:
                form.addError("Incorrect email address or password")
    else:
        form = SigninForm()
    
    print(form.non_field_errors())

    return render(
        request,
        "sign_in.html",  # "sing_in.html" yerine "sign_in.html" kullanın
        {
            "form": form,
            "user": user
        }
    )


def sign_out(request):
    try:
        del request.session["user"]
    except KeyError:
        pass
    return redirect("/")

def register(request):
    user = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
            )
            
            # ensure encrypted password
            user.set_password(form.cleaned_data["password"])

            try:
                user.save()
            except IntegrityError:
                form.addError(user.email + " is already a member")
            else:
                request.session["user"] = user.pk
                return redirect("/")
    else:
        form = UserForm()
    
    return render(
        request,
        "register.html",
        {
            "form": form,
            "months": range(1, 13),  # 1-12 arası ay sayıları
            "user": user,
            "years": range(2011, 2036),  # 2011-2035 arası yıl sayıları
        }
    )

def edit(request):
    uid = request.session.get('user')

    if uid is None:
        return redirect('/')

    user = User.objects.get(pk=uid)

    if request.method == 'POST':
        if form.is_valid():
            return redirect('/')

    else:
        form = UserForm()

    return render(
        request,
        'edit.html',
        {
            'form': form,
            'months': range(1, 12),
            'years': range(2011, 2036)
        },
    )