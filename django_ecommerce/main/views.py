from django.shortcuts import render
from users.models import User


# Create your views here.
def index(request):
    uid = request.session.get("user")
    if uid is None:
        return render(
        request,
        "index.html",
        {"user": False}
        )
    else:
        return render(
            request,
            "user.html",
            {"user": User.get_by_id(uid=uid)}
        )