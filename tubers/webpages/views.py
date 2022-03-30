from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    teams = Team.objects.all()
    sliders = Slider.objects.all()
    featuerd_youtubers = Youtuber.objects.order_by('-created_date').filter(is_feautured=True)
    latest_onboard = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders':sliders,
        'teams':teams,
        'featuerd_youtubers':featuerd_youtubers,
        'latest_onboard':latest_onboard,

    }
    return render(request,'webpages/home.html', data)

def about(request):
    return render(request,'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request,'webpages/contact.html')
