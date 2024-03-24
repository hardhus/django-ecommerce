from datetime import date, timedelta
from django.shortcuts import render
from main.models import Announcement, MarketingItem, StatusReport
from users.models import User


# Create your views here.
def index(request):
    uid = request.session.get("user")
    if uid is None:
        market_items = MarketingItem.objects.all()
        return render(
        request,
        "main/index.html",
        {"user": False}|
        {"marketing_items": market_items},
        )
    else:
        status = StatusReport.objects.all().order_by("-when")[:20]

        announce_date = date.today() - timedelta(days=30)
        announce = (Announcement.objects.filter(when__gte=announce_date).order_by("-when"))

        usr = User.get_by_id(uid)
        badges = usr.badges.all()

        return render(
            request,
            "main/user.html",
            {
                "user": usr,
                "badges": badges,
                "reports": status,
                "announce": announce,
            },
        )

def report(request):
    if request.method == "POST":
        status = request.POST.get("status", "")
        if status:
            uid = request.session.get("user")
            user = User.get_by_id(uid=uid)
            StatusReport(user=user, status=status).save()
        return index(request)