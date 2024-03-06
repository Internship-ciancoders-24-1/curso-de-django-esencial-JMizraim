from django.http import JsonResponse, HttpResponse

#utilities
from datetime import datetime

def hello_wold(request):
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Oh, hi! Current server time is {str(now)}")

def sorted(request):
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    numbers_list = list(map(lambda x : int(x),numbers.split(",")))
    numbers_list.sort()
    return JsonResponse({
        "result": numbers_list,
        "message": "Nice!"
    })
    
def say_hi(request, name, age):
    if age < 18:
        return HttpResponse(f"Sorrry {name}, you are not allowed here")
    return HttpResponse(f"Hi, {name}")