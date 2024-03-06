from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        "name": "Mont Blac",
        "user": "Yésica Cortés",
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "picture": "https://picsum.photos/200/200"
    },
        {
        "name": "Mont Blac",
        "user": "Yésica Cortés",
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "picture": "https://picsum.photos/200/200"
    }
]

# Create your views here.
def list_posts(request):
    return render(request, "feed.html", {"data": posts})