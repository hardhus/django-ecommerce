from django.shortcuts import render
from main.models import MarketingItem, StatusReport
from users.models import User


# Create your views here.
def index(request):
    uid = request.session.get("user")
    if uid is None:
        market_items = MarketingItem.objects.all()
        return render(
        request,
        "index.html",
        {"user": False}|
        {"marketing_items": market_items},
        )
    else:
        status = StatusReport.objects.all().order_by("-when")[:20]
        return render(
            request,
            "user.html",
            {"user": User.get_by_id(uid=uid)}|
            {"statuses": status},
        )

def report(request):
    if request.method == "POST":
        status = request.POST.get("status", "")
        if status:
            uid = request.session.get("user")
            user = User.get_by_id(uid=uid)
            StatusReport(user=user, status=status).save()
        return index(request)