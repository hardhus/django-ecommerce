import json
from django.http import HttpRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponseBadRequest
from django.shortcuts import HttpResponse, render, redirect
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

def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

def register(request: WSGIRequest):
    user = None
    if request.method == "POST":
        # We only talk AJAX posts now
        if is_ajax(request):
            return HttpResponseBadRequest("I only speak AJAX nowadays")

        data = json.loads(request.body.decode("utf-8"))
        form_data = {
            "name": data["name"]["$modelValue"],
            "email": data["email"]["$modelValue"],
            "password": data["password"]["$modelValue"],
            "ver_password": data["ver_password"]["$modelValue"],
        }
        form = UserForm(form_data)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                user = User.create(
                    cd["name"],
                    cd["email"],
                    cd["password"],
                )
            except IntegrityError:
                resp = json.dumps({
                    "status": "fail",
                    "errors": cd["email"] + " is already a member"
                })
            else:
                request.session["user"] = user.pk
                resp = json.dumps({
                    "status": "ok",
                    "url": "/",
                })
            return HttpResponse(resp, content_type="application/json")
        else: # form not valid
            resp = json.dumps({
                "status": "form-invalid",
                "errors": form.errors,
            })
            print(form.errors)
            return HttpResponse(resp, content_type="application/json")
    else:
        form = UserForm()

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