from django.shortcuts import render

from app.models import Activities, About, Contact, Sliders

# Create your views here.

def home(request):
    sliders=Sliders.objects.all
    abouts=About.objects.all
    contact=Contact.objects.all
    context={'abouts':abouts, 'contact':contact, 'sliders':sliders}
    return render(request, 'school/home.html', context)




def activities(request):
    activities=Activities.objects.all
    context={'activities':activities}
    return render(request, 'school/activities.html', context)

def activity(request,pk):
    activityObj=Activities.objects.get(id=pk)
    context={'activity':activityObj}
    return render(request, 'school/detail-activity.html', context)
