from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required 

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
@login_required
def list_posts(request):
    return render(request, "posts/feed.html", {"posts": posts})