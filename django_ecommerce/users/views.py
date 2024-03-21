from django.shortcuts import render, redirect
from users.forms import SigninForm, UserForm
from users.models import User
from django.template import RequestContext
from django.db import IntegrityError
import django_ecommerce.settings as settings
import datetime


# Create your views here.
def soon():
    soon = datetime.date.today() + datetime.timedelta(days=30)
    return {"month": soon.month, "year": soon.year}

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
        "users/sign_in.html",
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
            try:
                cd = form.cleaned_data
                user = User.create(
                    cd["name"],
                    cd["email"],
                    cd["password"],
                )
            except IntegrityError:
                print(form.cleaned_data)
                form.addError(cd["email"] + " is already a member")
            else:
                request.session["user"] = user.pk
                return redirect("/")
    else:
        form = UserForm()
    
    
    # TODO buradaki months ve years stripe olmadığından gereksiz mi acaba?
    # evet gereksiz
    return render(
        request,
        "users/register.html",
        {
            "form": form,
            "user": user,
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
        'users/edit.html',
        {
            'form': form,
            "user": user,
        },
    )